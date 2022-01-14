from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/Users/Imraj/AppData/Local/Google/Chrome/User Data/Default')
options.add_argument('--profile-directory=Default')

# Register the driver
chrome_browser = webdriver.Chrome(executable_path='/Users/Imraj/Desktop/Drivers/chromedriver', options=options)
chrome_browser.get('https://www.wix.com/dashboard/ad76b160-ef90-4e23-be35-cdb4993e92e2/store/orders/?referralInfo=sidebar')

latest_order = WebDriverWait(chrome_browser, 35).until(EC.element_to_be_clickable((By.XPATH, '//tr[@data-hook="order-row-0"]')))
latest_order.click()


client_name = WebDriverWait(chrome_browser, 35).until(EC.presence_of_element_located((By.XPATH, '//div[@data-hook="shipping-customer-name"]'))).text
client_address = WebDriverWait(chrome_browser, 35).until(EC.presence_of_element_located((By.XPATH, '//div[@data-hook="shipping-address-description"]'))).text
#product_name_1 = WebDriverWait(chrome_browser, 35).until(EC.presence_of_element_located((By.XPATH, '//span[@data-hook="product-line-name"]'))).text
product_quantity_1 = WebDriverWait(chrome_browser, 35).until(EC.presence_of_element_located((By.XPATH, '//div[@class="_2LbAw _1_Vxt _2y88X"]/div[2]'))).text
product_name_1 = WebDriverWait(chrome_browser, 35).until(EC.presence_of_element_located((By.XPATH, '//div[@id="root"]/div/div/div[2]/div/div/div/div/div/div/span/div/div/div/div[3]/div/div/div[8]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/span[1]'))).text
#product_2_quant = WebDriverWait(chrome_browser, 1).until(EC.presence_of_element_located((By.XPATH, '//[div@id="root"]/div/div/div[2]/div/div/div/div/div/div/span/div/div/div/div[3]/div/div/div[8]/div[1]/div[1]/div/div[2]/div[2]/div[4]/div[2]/span'))).text


def product_option():
    try:
        prod_option = WebDriverWait(chrome_browser, 1).until(EC.presence_of_element_located((By.XPATH, '//span[@data-hook="product-option"]'))).text
        return print('- {}'.format(prod_option))
    # this exception targets this specific timeoutexception error, hence why i imported it above.
    except TimeoutException:
        return ''

def additional_comments():
    try:
        add_comments = WebDriverWait(chrome_browser, 1).until(EC.presence_of_element_located((By.XPATH, '//span[@data-hook="buyer-note-content"]'))).text
        return {
            print("*Additional Comments:* {}".format(add_comments)),
            print()   
        }
    except TimeoutException:
        return ''

def quantity_identifier():

    if product_quantity_1 == 'x 1':
        return '1 x'
    elif product_quantity_1 == 'x 2':
        return '2 x'
    elif product_quantity_1 == 'x 3':
        return '3 x'
    elif product_quantity_1 == 'x 4':
        return '4 x'
    elif product_quantity_1 == 'x 5':
        return '5 x'
    else:
        return ''

def second_products():


    def foo():
        try:
            product_2_quant = WebDriverWait(chrome_browser, 1).until(EC.presence_of_element_located((By.XPATH, '//div[@id="root"]/div/div/div[2]/div/div/div/div/div/div/span/div/div/div/div[3]/div/div/div[8]/div[1]/div[1]/div/div[2]/div[2]/div[9]/div[2]/span'))).text
            return product_2_quant
        except TimeoutException:
            return ''

    def product_2_quantity():

        if foo() == 'x 1':
            return '1 x'
        elif foo() == 'x 2':
            return '2 x'
        elif foo() == 'x 3':
            return '3 x'
        elif foo() == 'x 4':
            return '4 x'
        elif foo() == 'x 5':
            return '5 x'
        else:
            return ''

    def product_2_option():
        
        try:
            prod_2_option = WebDriverWait(chrome_browser, 1).until(EC.presence_of_element_located((By.XPATH, '//div[@class="_2XCW_"]/div[7]/div/span[2]'))).text
            return print('- {}'.format(prod_2_option))
        except TimeoutException:
            return ''

    def product_name_2():

        try:
            product_2 = WebDriverWait(chrome_browser, 1).until(EC.presence_of_element_located((By.XPATH, '//div[@id="root"]/div/div/div[2]/div/div/div/div/div/div/span/div/div/div/div[3]/div/div/div[8]/div[1]/div[1]/div/div[2]/div[2]/div[7]/div/span'))).text
            return product_2
        except TimeoutException:
            return ''

    def part_invoice():

        return {
                print("{} {}".format(product_2_quantity(), product_name_2())),
                print(product_2_option())
            }

    return part_invoice()

client_contact_number = WebDriverWait(chrome_browser, 35).until(EC.presence_of_element_located((By.XPATH, '//div[@data-hook="shipping-customer-phone"]'))).text
delivery_method = WebDriverWait(chrome_browser, 35).until(EC.presence_of_element_located((By.XPATH, '//span[@data-hook="delivery-method-text"]'))).text


#remember this /div[2] to get to the second div class of the "payment-summary-shipping", in order to navigate your way through similar classes
subtotal = WebDriverWait(chrome_browser, 35).until(EC.presence_of_element_located((By.XPATH, '//div[@data-hook="payment-summary-subtotal"]/div[2]'))).text
delivery_cost = WebDriverWait(chrome_browser, 35).until(EC.presence_of_element_located((By.XPATH, '//div[@data-hook="payment-summary-shipping"]/div[2]'))).text
delivery_timing = WebDriverWait(chrome_browser, 35).until(EC.presence_of_element_located((By.XPATH, '//span[@data-hook="delivery-method-date"]'))).text
total = WebDriverWait(chrome_browser, 35).until(EC.presence_of_element_located((By.XPATH, '//div[@data-hook="payment-summary-total"]/div[2]'))).text



def invoice_gen():

    if product_name_1 == 'Jager/Soju Bundle':

        return [
            print("*Invoice  * "),
            print(),
            print("Name: {}".format(client_name)),
            print("Address: {}".format(client_address)),
            print("Contact Number: {}".format(client_contact_number)),
            print(),
            print("Product(s): "),
            print(),
            print("{} {}".format(quantity_identifier(), product_name_1)),
            product_option(),
            print('- 1 x Soju'),
            print('- 1 x Jagermeister'),
            print('- 3 x Red Bull '),
            second_products(),
            print("*Delivery Method: {}*".format(delivery_method)),
            print("*Delivery Timing: {}*".format(delivery_timing)),
            print(),
            additional_comments(),
            print("Subtotal: {}".format(subtotal)),
            print("Delivery cost: {}".format(delivery_cost)),
            print("Total: {}".format(total))
        ]

    elif product_name_1 == 'Party Bomb Special':
        return [

            print("*Invoice  * "),
            print(),
            print("Name: {}".format(client_name)),
            print("Address: {}".format(client_address)),
            print("Contact Number: {}".format(client_contact_number)),
            print(),
            print("Product(s): "),
            print(),
            print("{} Party Bomb Special".format(quantity_identifier())),
            print('- 1 x Chivas Regal 12'),
            print('- 1 x Jagermeister'),
            print('- 1 x Coke 1.5L'),
            print('- 2 x Red Bull'),
            second_products(),
            print("*Delivery Method: {}*".format(delivery_method)),
            print("*Delivery Timing: {}*".format(delivery_timing)),
            print(),
            additional_comments(),
            print("Subtotal: {}".format(subtotal)),
            print("Delivery cost: {}".format(delivery_cost)),
            print("Total: {}".format(total))
        ]
    elif product_name_1 == 'Scotland X America':
        return [

            print("*Invoice  * "),
            print(),
            print("Name: {}".format(client_name)),
            print("Address: {}".format(client_address)),
            print("Contact Number: {}".format(client_contact_number)),
            print(),
            print("Product(s): "),
            print(),
            print("{} {}".format(quantity_identifier(), product_name_1)),
            print('- 2 x Coke 1.5L'),
            print('- 1 x Chivas 12'),
            print("- 1 x Jack Daniel's"),
            second_products(),
            print("*Delivery Method: {}*".format(delivery_method)),
            print("*Delivery Timing: {}*".format(delivery_timing)),
            print(),
            additional_comments(),
            print("Subtotal: {}".format(subtotal)),
            print("Delivery cost: {}".format(delivery_cost)),
            print("Total: {}".format(total))
        ]
    elif product_name_1 == 'Sojulicious (8 Bottles)':
        return [

            print("*Invoice  * "),
            print(),
            print("Name: {}".format(client_name)),
            print("Address: {}".format(client_address)),
            print("Contact Number: {}".format(client_contact_number)),
            print(),
            print("Product(s): "),
            print(),
            print("{} {}".format(quantity_identifier(), product_name_1)),
            print('- 8 x {}'.format(product_option())),
            second_products(),
            print("*Delivery Method: {}*".format(delivery_method)),
            print("*Delivery Timing: {}*".format(delivery_timing)),
            print(),
            additional_comments(),
            print("Subtotal: {}".format(subtotal)),
            print("Delivery cost: {}".format(delivery_cost)),
            print("Total: {}".format(total))
        ]
    elif product_name_1 == 'Soju Bundle of 6':
        return [

            print("*Invoice  * "),
            print(),
            print("Name: {}".format(client_name)),
            print("Address: {}".format(client_address)),
            print("Contact Number: {}".format(client_contact_number)),
            print(),
            print("Product(s): "),
            print(),
            print("{} {}".format(quantity_identifier(), product_name_1)),
            product_option(),
            print('- 6 x Soju'),
            second_products(),
            print("*Delivery Method: {}*".format(delivery_method)),
            print("*Delivery Timing: {}*".format(delivery_timing)),
            print(),
            additional_comments(),
            print("Subtotal: {}".format(subtotal)),
            print("Delivery cost: {}".format(delivery_cost)),
            print("Total: {}".format(total))
        ]
    else:
        return [

            print("*Invoice  * "),
            print(),
            print("Name: {}".format(client_name)),
            print("Address: {}".format(client_address)),
            print("Contact Number: {}".format(client_contact_number)),
            print(),
            print("Product(s): "),
            print(),
            print("{} {}".format(quantity_identifier(), product_name_1)),
            product_option(),
            second_products(),
            print("*Delivery Method: {}*".format(delivery_method)),
            print("*Delivery Timing: {}*".format(delivery_timing)),
            print(),
            additional_comments(),
            print("Subtotal: {}".format(subtotal)),
            print("Delivery cost: {}".format(delivery_cost)),
            print("Total: {}".format(total))
        ]

invoice_gen()

