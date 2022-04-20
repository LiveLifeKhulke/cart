from selenium import webdriver


def before_scenario(context,driver):
    context.driver= webdriver.Firefox(executable_path='c:\\geckodriver.exe')

def after_step(context,step):
    print()