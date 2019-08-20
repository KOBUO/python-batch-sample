import time
from functools import wraps
import pandas as pd
from pandas import DataFrame


def stop_watch(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        process_time = time.time() - start
        print("{0:10}:{1:10.5f}秒".format(func.__name__, process_time))
        return result

    return wrapper


@stop_watch
def create_at(data: DataFrame) -> DataFrame:
    _data = data.copy()
    calculate = calculate_at()
    _data.loc[:, 'angle_diff'] = [calculate(angle) for angle in _data.angle.tolist()]
    return _data


def calculate_at(default: float = 0.0):
    _angle: float = default

    def calculate(angle: float) -> float:
        nonlocal _angle
        _angle = angle - _angle
        return _angle

    return calculate


@stop_watch
def main():
    pd.set_option('display.max_columns', 10)
    df = stop_watch(pd.read_csv)('./generate/data/machine_item.csv')
    create_at(df)


if __name__ == '__main__':
    main()
