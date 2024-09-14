import pandas as pd
import matplotlib.pyplot as plt
import easygui

data = pd.read_csv("D:\\Project-Ip\\car_sales_data_2.csv")

def read_csv():
    print(data)

def display_menu():
    print("      Car Sales Analysis Menu:")
    print("      1. Car Type Wise Distribution (Pie)")
    print("      2. Car Sales by Car Make (Pie)")
    print("      3. Salesperson-wise Commission Earned (Bar)")
    print("      4. Year-wise Car Sales (Bar)")
    print("      5. Year-wise Car Sales by Make (Line)")
    print("      6. Exit to Main Menu")

def display_mainmenu():
    print("1. Introduction")
    print("2. Read csv")
    print("3. Max Sales")
    print("4. Graphical Analysis")
    print("5. Credit (Developers)")
    print("6. Exit")



def car_type_wise_distribution():
    car_type_count = data['Car Type'].value_counts()

    explode = [0.1 if i == 0 else 0.1 for i in range(len(car_type_count))]

    # Creating a pie chart with an exploded slice
    plt.figure(figsize=(8, 8))
    plt.pie(car_type_count, labels=car_type_count.index, autopct='%1.1f%%', startangle=140, explode=explode)
    plt.title('Distribution of Car Types')
    plt.axis('equal')  

    plt.tight_layout()
    plt.show()

def car_sales_by_make_menu():
    car_make_sales = data.groupby('Car Make')['Sale Price'].sum().sort_values()

    
    plt.figure(figsize=(8, 8))
    plt.pie(car_make_sales, labels=car_make_sales.index, autopct='%1.1f%%', startangle=140)
    plt.title('Car Make-wise Sales Distribution')
    plt.axis('equal')  

    plt.tight_layout()
    plt.show()

def salesperson_wise_commission_menu():
    salesperson_commission = data.groupby('Salesperson')['Commission Earned'].sum().sort_values()

    # Creating a bar plot for salesperson-wise commissions
    plt.figure(figsize=(10, 6))
    salesperson_commission.plot(kind='barh', color='skyblue')
    plt.title('Salesperson-wise Commission Earned')
    plt.xlabel('Total Commission Earned')
    plt.ylabel('Salesperson')
    plt.grid(axis='x')  # Adding gridlines along the x-axis for better readability

    plt.tight_layout()
    plt.show()

def year_wise_sales_menu():
    data['Date'] = pd.to_datetime(data['Date'])

    data['Month'] = data['Date'].dt.strftime('%b %Y') 
    

    month_wise_sales = data.groupby('Month')['Sale Price'].sum()
    month_wise_sales = month_wise_sales.reset_index()

    month_wise_sales['Date'] = pd.to_datetime(month_wise_sales['Month'], format='%b %Y')
    month_wise_sales = month_wise_sales.sort_values('Date')
    month_wise_sales.set_index('Month', inplace=True)
    del month_wise_sales['Date']

    plt.figure(figsize=(10, 5))

    month_wise_sales.plot(kind='bar', color='skyblue')
    plt.title('Month-wise Sales of Cars')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=90)

    plt.tight_layout()
    plt.show()

def car_sales_count_year_wise_by_car_make():
    data['Date'] = pd.to_datetime(data['Date'])

    
    data['Month'] = data['Date'].dt.month
    data['Year'] = data['Date'].dt.year

    
    car_make_month_year_count = data.groupby(['Car Make', 'Year', 'Month']).size().reset_index(name='Count')

    
    plt.figure(figsize=(12, 6))

    
    for car_make, df in car_make_month_year_count.groupby('Car Make'):
        plt.plot(df['Year'].astype(str) + '-' + df['Month'].astype(str), df['Count'], marker='o', label=car_make)

    plt.title('Month and Year-wise Count of Car Sales for Each Car Make')
    plt.xlabel('Year-Month')
    plt.ylabel('Count of Sales')
    plt.xticks(rotation=45)  # Rotating x-axis labels for better readability
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def showcreditpage():
    credit_info = """
    ****************************************
    ** Developer: Yash Saxena             ** 
    ** Class: XII-B (2023-24)             **
    ** School: B.V.B., Vidyashram School  **
    ** Address: K.M.Munshi Marg, Jaipur   **
    ****************************************
    
    """
    easygui.msgbox(credit_info, title="Credit (Developer)")



def show_introduction():
    introduction_text = """
    Maintaining a competitive edge in the automotive sector necessitates an in-depth understanding of market trends, consumer inclinations, and sales dynamics. Our objective as we begin this research is to carefully examine vehicle sales data for the years 2022 and 2023, revealing the complex relationships between month-by-month, salesperson-by-month, and model-by-month factors.
    The automotive industry is a symphony of industry innovation, sales strategy, and consumer demand. It is not simply about moving cars. We want to find patterns, spikes, and lulls in the month-to-month sales data that can be useful in determining future production and marketing plans. Comprehending the fluctuations in customer behavior over this period will be essential to our understanding.
    Furthermore, breaking down salesperson-specific data will provide us a detailed understanding of individual performances, enabling us to identify high performers, areas in need of development, and customer-resonant methods. We will be able to correlate performance with sales strategies thanks to this micro-level study, which will provide insightful information for optimizing sales teams.
    Regarding the models, we will concentrate on identifying the car models that have made a name for themselves and figuring out what makes them successful. In addition to enabling manufacturers to improve the products they offer, this analysis will help dealerships better align their inventory with customer needs.
    Our mission is to convert unprocessed data into useful information so that decision-makers in the automobile industry may make well-informed choices. We want to shed light on the future for companies in this fast-paced, fiercely competitive sector as we make our way through the complex web of vehicle sales statistics for 2022 and 2023
    """
    easygui.msgbox(introduction_text, title="Introduction")

def max_sales():
    data['Date'] = pd.to_datetime(data['Date'])

    
    max_sales_data = data.groupby('Car Make')['Sale Price'].sum().reset_index()

    max_sales_data = max_sales_data.sort_values(by='Sale Price', ascending=False)
    print(max_sales_data)

# Sub program
def showmenu():
    while True:
        display_menu()
        choice = input("Please enter your choice (1-6): ")

        if choice == '1':
            car_type_wise_distribution()
        elif choice == '2':
            car_sales_by_make_menu()
        elif choice == '3':
            salesperson_wise_commission_menu()
        elif choice == '4':
            year_wise_sales_menu()
        elif choice == '5':
            car_sales_count_year_wise_by_car_make()
        elif choice == '6':
            print("Thank you for using the Car Sales Analysis Menu!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

while True:
    display_mainmenu()
    choice = input("Please enter your choice (1-6): ")

    if choice == '1':
        show_introduction()
    elif choice == '2':
        read_csv()
    elif choice == '3':
        max_sales()
    elif choice == '4':
        showmenu()
    elif choice == '5':
        showcreditpage()
    elif choice == '6':
        print("Thank you for using the Car Analysis App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
