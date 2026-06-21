import pandas as pd
retail_data = {
    "Product Name": [
        "Laptop", "Mouse", "Keyboard", "Headphones", "Monitor","Mouse","Keyboard",
        "Smartphone", "Printer", "USB Cable", "Tablet", "Camera","Camera"
    ],

    "Category": [
        "Electronics", "Accessories", "Accessories", "Accessories", "Electronics","Accessories","Accessories",
        "Electronics", "Office", "Accessories", "Electronics", "Electronics","Electronics"
    ],

    "Price": [
        25000, 300, 800, 1500, 5000,300,800,
        12000, 3500, 100, 9000, 15000,15000
    ],

    "Quantity Sold": [
        15, 80, 40, 25, 12,14,20,
        20, 8, 100, 10, 6, 2
    ],

    "City": [
        "Cairo", "Alexandria", "Giza", "Cairo", "Asyut","Cairo","Asyut",
        "Cairo", "Mansoura", "Giza", "Alexandria", "Cairo","Mansoura"
    ]
}
data=pd.DataFrame(retail_data,index=["the first product","the second product","the third product","the fourd product","the fifth product","the sixth product","the seventh product","the eighth product","the ninth product","the tenth product","the eleventh product","the twelfth product","the thirteenth product"])
data["Revenue"]=data["Price"]*data["Quantity Sold"]
print(data)
print("\n Sales Analysis ")
the_highest_Sold_product=data["Quantity Sold"].idxmax()
print(f"the highest sold product : {data.loc[the_highest_Sold_product,"Product Name"]}")
the_lowest_Sold_product=data["Quantity Sold"].idxmin()
print(f"the lowest sold product : {data.loc[the_lowest_Sold_product,"Product Name"]}")
print(f"Total Quantity Sold : {data["Quantity Sold"].sum()}")
print(f"Average Quantity Sold  : {data["Quantity Sold"].mean()}")
Average_Quantity_Sold=data.groupby("Product Name")["Quantity Sold"].mean()
print(f"Average Quantity Sold (all products) : ")
print(Average_Quantity_Sold)
data11=data[data["Product Name"]=="Laptop"]
print(f"Average Quantity Sold (Laptop) : {data11["Quantity Sold"].mean()}")
data11=data[data["Product Name"]=="Camera"]
print(f"Average Quantity Sold (Camera) :  {data11["Quantity Sold"].mean()}")
print("\n Revnue Analysis ")
the_highest_Revenue_product=data["Revenue"].idxmax()
print(f"the highest Revenue product   : {data.loc[the_highest_Revenue_product,"Product Name"]}")
print(f"the highest Revenue : {data["Revenue"].max()}")
the_lowest_Revenue_product=data["Revenue"].idxmin()
print(f"the lowest Revenue product   : {data.loc[the_lowest_Revenue_product,"Product Name"]}")
print(f"the lowest Revenue : {data["Revenue"].min()}")
print(f"Total Retail Revenue: {data["Revenue"].sum()}")
print(f"Average  revenue (all products) :")
data1111=data.groupby("Product Name")["Revenue"].mean()
print(data1111)
data6=data[data["Product Name"]=="Camera"]
print(f"the average Revenue (Camera) : {data6["Revenue"].mean()}")
data7=data[data["Product Name"]=="Laptop"]
print(f"the average Revenue (Laptop) : {data7["Revenue"].mean()}")
data8=data[data["Product Name"]=="Keyboard"]
print(f"the average Revenue (Keyboard) : {data8["Revenue"].mean()}")
print("averge Quantity sold by  city :  ")
data9=data.groupby("City")["Quantity Sold"].mean()
print(data9)
print("Total Quantity sold  (all cities) :  ")
data10=data.groupby("City")["Quantity Sold"].sum()
print(data10)
data99=data[data["City"]=="Cairo"]
print(f"Total Quantity sold in Cairo: {data99["Quantity Sold"].sum()}")
data100=data[data["City"]=="Alexandria"]
print(f"Total Quantity sold in Alexandria: {data100["Quantity Sold"].sum()}")
data101=data[data["City"]=="Giza"]
print(f"Total Quantity sold in Giza: {data101["Quantity Sold"].sum()}")
data102=data[data["City"]=="Asyut"]
print(f"Total Quantity sold in Asyut: {data102["Quantity Sold"].sum()}")
data103=data[data["City"]=="Mansoura"]
print(f"Total Quantity sold in Mansoura: {data103["Quantity Sold"].sum()}")
data99=data[data["City"]=="Cairo"]
print(f"Average Revenue in Cairo: {data99["Revenue"].mean()}")
data5555=data.groupby("City")["Revenue"].mean()
print(f"Average Revenue all cities : ")
print(data5555)
print("\n Category Analysis ")
Best_Selling_Category=data.groupby("Category")["Quantity Sold"].sum()
Best_Selling_Category1=Best_Selling_Category.idxmax()
print(f"Best Selling Category  : {Best_Selling_Category1,Best_Selling_Category.max()}")
Worst_Performing_Category=Best_Selling_Category.idxmin()
print(f"Worst Performing Category  : {Worst_Performing_Category,Best_Selling_Category.min()}")
print(f"Best Selling Category  : {Best_Selling_Category1}")
print(f"Worst Performing Category  : {Worst_Performing_Category}")
print(Best_Selling_Category)
Category_with_the_Highest_Revenue=data.groupby("Category")["Revenue"].sum()
Category_with_the_Highest_Revenue1=Category_with_the_Highest_Revenue.max()
Category_with_the_Highest_Revenue2=Category_with_the_Highest_Revenue.idxmax()
print(Category_with_the_Highest_Revenue)
print(f"Category with the highest revenue :  {Category_with_the_Highest_Revenue2,Category_with_the_Highest_Revenue1}")
print(f"Category with the highest revenue :  {Category_with_the_Highest_Revenue2}")
Category_with_the_Highest_Revenue1=Category_with_the_Highest_Revenue.min()
Category_with_the_Highest_Revenue2=Category_with_the_Highest_Revenue.idxmin()
print(f"Category with the lowest revenue :  {Category_with_the_Highest_Revenue2,Category_with_the_Highest_Revenue1}")
print(f"Category with the lowest revenue :  {Category_with_the_Highest_Revenue2}")
data.to_csv("retail_data.csv",index=True)
data10.to_csv("retail_data1.csv",index=True)
data1111.to_csv("retail_data2.csv",index=True)




