"""
Test for the ETL and query functions.
"""

import subprocess


def test_extract():
    """tests extract()"""
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_transform_load():
    """tests transform_load()"""
    result = subprocess.run(
        ["python", "main.py", "transform_load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout


def test_general_query():
    """tests general_query with the births datasets"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "general_query",
            """SELECT t1.day_of_week,
                      AVG(t1.births) as avg_daily_births,
                      COUNT(*) as total_days_recorded
                 FROM default.births2000 t1
                 JOIN default.births1994 t2 ON t1.year = t2.year
                 GROUP BY t1.day_of_week
                 ORDER BY avg_daily_births DESC
                 LIMIT 3""",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_general_query()