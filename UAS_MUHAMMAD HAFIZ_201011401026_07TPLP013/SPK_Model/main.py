import sys
from colorama import Fore, Style
from models import Base, Smartphones
from engine import engine
from sqlalchemy import select
from sqlalchemy.orm import Session
from settings import (
    DEV_SCALE_model, DEV_SCALE_ram, DEV_SCALE_processor,
    DEV_SCALE_storage, DEV_SCALE_battery_capacity,
    DEV_SCALE_price, DEV_SCALE_screen_size
)

session = Session(engine)


def create_table():
    Base.metadata.create_all(engine)
    print(f'{Fore.GREEN}[Success]: {Style.RESET_ALL}Database has created!')


class BaseMethod():

    def __init__(self):
        self.raw_weight = {
            'model': 5,
            'ram': 3,
            'processor': 4,
            'storage': 3,
            'battery_capacity': 4,
            'screen_size': 3,
            'price': 1
        }

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {k: v / total_weight for k, v in self.raw_weight.items()}

    @property
    def data(self):
        query = select(Smartphones)
        return [{'id': smartphones.id, 
        'model': DEV_SCALE_model[smartphones.model], 
        'ram': DEV_SCALE_ram[smartphones.ram], 
        'processor': DEV_SCALE_processor[smartphones.processor], 
        'storage': DEV_SCALE_storage[smartphones.storage], 
        'battery_capacity': DEV_SCALE_battery_capacity[smartphones.battery_capacity], 
        'screen_size': DEV_SCALE_screen_size[smartphones.screen_size], 
        'price': DEV_SCALE_price[smartphones.price]} 
        for smartphones in session.scalars(query)]

    @property
    def normalized_data(self):
        max_values = {
            'model': max(data['model'] for data in self.data),
            'ram': max(data['ram'] for data in self.data),
            'processor': max(data['processor'] for data in self.data),
            'storage': max(data['storage'] for data in self.data),
            'battery_capacity': max(data['battery_capacity'] for data in self.data),
            'screen_size': max(data['screen_size'] for data in self.data),
            'price': min(data['price'] for data in self.data)
        }

        return [
            {
                'id': data['id'],
                'model': data['model'] / max_values['model'],
                'ram': data['ram'] / max_values['ram'],
                'processor': data['processor'] / max_values['processor'],
                'storage': data['storage'] / max_values['storage'],
                'battery_capacity': data['battery_capacity'] / max_values['battery_capacity'],
                'screen_size': data['screen_size'] / max_values['screen_size'],
                'price': max_values['price'] / data['price']
            } for data in self.data
        ]


class WeightedProduct(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        result = {
            row['id']: round(
                row['model'] ** weight['model'] *
                row['ram'] ** weight['ram'] *
                row['processor'] ** weight['processor'] *
                row['storage'] ** weight['storage'] *
                row['battery_capacity'] ** weight['battery_capacity'] *
                row['screen_size'] ** (-weight['screen_size']) *
                row['price'] ** weight['price'], 2
            )
            for row in self.normalized_data
        }
        return dict(sorted(result.items(), key=lambda x: x[1], reverse=True))


class SimpleAdditiveWeighting(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        result = {
            row['id']: round(
                row['model'] ** weight['model'] *
                row['ram'] ** weight['ram'] *
                row['processor'] ** weight['processor'] *
                row['storage'] ** weight['storage'] *
                row['battery_capacity'] ** weight['battery_capacity'] *
                row['screen_size'] ** (-weight['screen_size']) *
                row['price'] ** weight['price'], 2
            )
            for row in self.normalized_data
        }
        return dict(sorted(result.items(), key=lambda x: x[1]))


def run_saw():
    saw = SimpleAdditiveWeighting()
    print('result:', saw.calculate)


def run_wp():
    wp = WeightedProduct()
    print('result:', wp.calculate)


if len(sys.argv) > 1:
    arg = sys.argv[1]

    if arg == 'create_table':
        create_table()
    elif arg == 'saw':
        run_saw()
    elif arg == 'wp':
        run_wp()
    else:
        print('command not found')
