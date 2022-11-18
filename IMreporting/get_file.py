"""
Module to read file name and calculate
"""

import os
import sys
import logging
from typing import Dict, List, Tuple
import csv

_logger = logging.getLogger(__name__)


class Tasks:
    """
    Contains methods to read inputs and calculation to create reports
    """

    def __init__(self, name, price, lot_size):
        """
        object product
        :param name: product name
        :param price:
        :param lot_size:
        """
        self.name = name
        self.price = price
        self.lot_size = lot_size

    @classmethod
    def generate_report(cls, team_map, product, sales, team_report, prod_report):
        """
        read and generate report after calculation)
        :param team_map:
        :param product:
        :param sales:
        :param team_report:
        :param prod_report:
        :return:
        """
        team_mapped = cls.create_team_map(team_map)
        product_mapped = cls.create_product_map(product)

    @staticmethod
    def create_team_map(team_map) -> dict:
        """

        :param team_map: TeamMap.cvs
        :return:
        """
        team_mapped = {}

        with open(team_map, 'r') as team_file:
            next(team_file)
            for line in team_file:
                team_mapped[line[0]] = line[1]  # teamId, teamName map

        return team_mapped

    @staticmethod
    def create_product_map(product) -> dict:
        """
        read ProductMaster and create product object
        :param product: ProductMaster.csv
        :return:
        """
        product_map = {}

        with open(product, 'r') as product_file:
            # create a new instance of product object and in the map
            for line in product_file:
                product_map[line[1]] = Tasks(line[2], line[3], line[4])

        return product_map

    @staticmethod
    def get_price(product_id):
        """

        :param product_id:
        :return:
        """
        product =
