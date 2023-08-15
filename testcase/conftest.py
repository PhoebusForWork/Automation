
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    passed_count = len(terminalreporter.stats.get('passed', []))
    failed_count = len(terminalreporter.stats.get('failed', []))
    skipped_count = len(terminalreporter.stats.get('skipped', []))
    error_count = len(terminalreporter.stats.get('error', []))
    xfailed_count = len(terminalreporter.stats.get('xfailed', []))
    xpassed_count = len(terminalreporter.stats.get('xpassed', []))
    total_count = passed_count + failed_count + skipped_count + error_count + xfailed_count + xpassed_count

    print(f"Total tests: {total_count}")
    print(f"Passed tests: {passed_count}")
    print(f"Failed tests: {failed_count}")
    print(f"Skipped tests: {skipped_count}")
    print(f"Error tests: {error_count}")
    print(f"Expected failures: {xfailed_count}")
    print(f"Unexpected passes: {xpassed_count}")

    summary_text = f"Total tests: {total_count}\n"
    summary_text += f"Passed tests: {passed_count}\n"
    summary_text += f"Failed tests: {failed_count}\n"
    summary_text += f"Skipped tests: {skipped_count}\n"
    summary_text += f"Error tests: {error_count}\n"
    summary_text += f"Expected failures: {xfailed_count}\n"
    summary_text += f"Unexpected passes: {xpassed_count}\n"

    with open('result_summary.txt', 'w') as file:
        file.write(summary_text)
