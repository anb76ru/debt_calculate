import pytest

from main_app import calculate

data = [
    (
        {'qwe': {'Затраты': 5000.0, 'Долг': -3288.75},
         'asd': {'Затраты': 1500.0, 'Долг': 211.25},
         'zxc': {'Затраты': 345.0, 'Долг': 1366.25},
         'tyu': {'Затраты': 0.0, 'Долг': 1711.25}
         },
        [
            '\ntyu Переводит qwe 1711.25',
            '\nzxc Переводит qwe 1366.25',
            '\nasd Переводит qwe 211.25'
        ]
    ),
    (
        {'qwe': {'Затраты': 156, 'Долг': -79.67},
         'asd': {'Затраты': 48, 'Долг': 28.33},
         'zxc': {'Затраты': 25, 'Долг': 51.33}
         },
        [
            '\nzxc Переводит qwe 51.33',
            '\nasd Переводит qwe 28.33'
        ]
    )
]


class TestApp:

    @pytest.mark.parametrize('members', data)
    def test_app(self, members):

        assert calculate(members[0]) == members[1]
