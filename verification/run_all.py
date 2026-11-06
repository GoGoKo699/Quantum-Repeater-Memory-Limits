#!/usr/bin/env python3
"""Run the three finite scientific checks and record their environment/results.

From the repository root: python verification/run_all.py [--no-plot]
This wrapper adds no scientific tests; it invokes the three standalone scripts.
"""
from __future__ import annotations
import argparse
import importlib.metadata
import json
from pathlib import Path
import platform
import subprocess
import sys

BASE = Path(__file__).resolve().parent
RESULTS = BASE / 'results'


def package_version(name):
    try:
        return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        return None


def main(make_plot=True):
    if sys.flags.optimize:
        raise SystemExit('Run without -O: the finite checks use Python assertions.')
    RESULTS.mkdir(parents=True, exist_ok=True)
    steps = [
        ('check_repeater_small.py', []),
        ('check_finite_bounds.py', []),
        ('repeater_bounds.py', ['--plot'] if make_plot else []),
    ]
    report = {
        'python_version': platform.python_version(),
        'implementation': platform.python_implementation(),
        'packages': {'numpy': package_version('numpy'),
                     'matplotlib': package_version('matplotlib')},
        'plot_requested': make_plot,
        'commands': [],
    }
    manifest = RESULTS / 'run_summary.json'
    for script, arguments in steps:
        public_command = ' '.join(['python', f'verification/{script}', *arguments])
        print(f'Running {public_command}', flush=True)
        completed = subprocess.run(
            [sys.executable, str(BASE / script), *arguments],
            cwd=BASE.parent, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, check=False,
        )
        log = RESULTS / (Path(script).stem + '.log')
        log.write_text(completed.stdout)
        report['commands'].append({
            'command': public_command,
            'returncode': completed.returncode,
            'log': f'verification/results/{log.name}',
        })
        manifest.write_text(json.dumps(report, indent=2) + '\n')
        if completed.returncode:
            print(completed.stdout, end='')
            raise SystemExit(completed.returncode)
        print(f'Passed; full output: verification/results/{log.name}', flush=True)

    small = json.loads((RESULTS / 'check_repeater_small_results.json').read_text())
    finite = json.loads((RESULTS / 'finite_bound_checks.json').read_text())
    bounds = json.loads((RESULTS / 'repeater_bounds.json').read_text())
    report['results'] = {
        'integer_profile_cases': len(small['profile_checks']),
        'exact_threshold_cases': len(small['strict_tv_threshold_checks']),
        'swap_parameter_cases': len(small['one_and_two_swap_checks']),
        'bell_outcome_branches': sum(x['all_bell_outcomes_checked']
                                    for x in small['one_and_two_swap_checks']),
        'largest_frobenius_state_error': max(x['max_frobenius_state_error']
                                            for x in small['one_and_two_swap_checks']),
        'largest_outcome_probability_error': max(x['max_outcome_probability_error']
                                                for x in small['one_and_two_swap_checks']),
        'finite_shell_entropy_cases': finite['checks']['cases'],
        'largest_log_bound_excess': finite['checks']['largest_log_bound_excess'],
        'analytic_visibility_cases': len(bounds['analytic_recursion_checks']),
        'largest_visibility_discrepancy': max(x['discrepancy']
                                            for x in bounds['analytic_recursion_checks']),
        'sublinear_exponent_rows': len(bounds['sublinear_exponent_bounds']),
        'asap_noise_rows': len(bounds['asap_noise_comparison']),
        'linear_coefficient_rows': len(bounds['linear_coefficient_bounds']),
        'weighted_bound_example': finite['weighted_bound_example'],
    }
    manifest.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--no-plot', action='store_true',
                        help='run all numerical checks without creating the figure')
    main(make_plot=not parser.parse_args().no_plot)
