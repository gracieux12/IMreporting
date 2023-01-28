"""
Module to read from files ands use the data to produce 2 output
"""
from collections import defaultdict
from email.policy import default
import os
import sys
import logging
from typing import Dict, List, Tuple
import csv

_logger = logging.getLogger(__name__)

class TeamMap:
    """
    contains Team Map values
    """
    def __init__(self, teamId: int, name: str) -> None:
        
        self.teamId = teamId
        self.name = name
        

class ProductMap:
    def __init__(self, productId, name, price, lotSize) -> None:
        self.productId = productId
        self.name = name
        self.price = price
        self.lotSize = lotSize

class Sales:
    def __init__(self, saleId, productId, teamId, quantity, discount) -> None:
        self.saleId = saleId
        self.productId = productId
        self.teamId = teamId
        self.quantity = quantity
        self.discount = discount


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
        team_mapped = cls.create_team_maps(team_map)
        product_mapped = cls.create_product_maps(product)
        sales_mapped = cls.create__sales(sales)

        # Team report
        sales_map = defaultdict(int)
        product_map = {}
        for sale in sales_mapped:
            # Get team name
            team_name = [team.name for team in team_mapped if team.teamId == sale.teamId][0]
            price = [product.price for product in product_mapped if product.productId == sale.productId][0]
            product_name = [product.name for product in product_mapped if product.productId == sale.productId][0]
            gross_revenue = float(price) * float(sale.quantity)

            sales_map[team_name] += gross_revenue

            if product_name not in product_map:
                product_map[product_name] = [0,0,0]

            product_map[product_name][0] += gross_revenue
            product_map[product_name][1] += int(sale.quantity)
            product_map[product_name][2] += float(sale.discount)



        open_file = open(team_report, 'w', newline="")
        writer = csv.writer(open_file)
        for key, value in sales_map.items():
            writer.writerow([key, value])

        # Product report
        open_file = open(prod_report, 'w', newline="")
        writer = csv.writer(open_file)
        for key, value in product_map.items():
            writer.writerow([key, value])
            

    @staticmethod
    def create_team_maps(team_map) -> list:
        """

        :param team_map: TeamMap.cvs
        :return:
        """
        team_mapped = []

        with open(team_map, 'r') as team_file:
            next(team_file)
            for line in team_file:
                line  = line.split(",")
                team = TeamMap(line[0], line[1])
                team_mapped.append(team)

        return team_mapped

    @staticmethod
    def create_product_maps(product) -> list:
        """
        read ProductMaster and create product object
        :param product: ProductMaster.csv
        :return:
        """
        product_maps = []

        with open(product, 'r') as product_file:
            # create a new instance of product object and in the map
            for line in product_file:
                line  = line.split(",")
                productMap = ProductMap(line[0], line[1], line[2], line[3])
                product_maps.append(productMap)

        return product_maps

    @staticmethod
    def create__sales(sale) -> list:
        """
        read ProductMaster and create product object
        :param product: ProductMaster.csv
        :return:
        """
        sales_maps = []

        with open(sale, 'r') as sale_file:
            # create a new instance of product object and in the map
            for line in sale_file:
                line  = line.split(",")
                sale = Sales(line[0], line[1], line[2], line[3], line[4])
                sales_maps.append(sale)
        return sales_maps

    # @staticmethod
    # def get_price(product_id):
    #     """

    #     :param product_id:
    #     :return:
    #     """
    #     product =

    print("hi")
