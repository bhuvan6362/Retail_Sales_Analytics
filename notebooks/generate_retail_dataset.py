import pandas as pd
import random
import numpy as np
from datetime import datetime, timedelta
import os, shutil

# reproducibility
random.seed(42)
np.random.seed(42)

# Parameters for small and large datasets
sizes = {
    "small": {"n_customers": 200, "n_products": 50, "n_orders": 1000},
    "large": {"n_customers": 2000, "n_products": 200, "n_orders": 12000}
}

def generate_dataset(n_customers, n_products, n_orders, prefix, out_dir):
    # Customers
    regions = ["North", "South", "East", "West"]
    genders = ["Male", "Female"]
    segments = ["Consumer", "Corporate", "Home Office"]
    customers = pd.DataFrame({
        "customer_id": [f"{prefix}C{1000+i}" for i in range(n_customers)],
        "age": np.random.randint(18,65,n_customers),
        "gender": np.random.choice(genders, n_customers),
        "region": np.random.choice(regions, n_customers),
        "segment": np.random.choice(segments, n_customers)
    })
    
    # Products
    categories = ["Technology", "Furniture", "Office Supplies"]
    subcats = {
        "Technology": ["Phones", "Accessories", "Copiers"],
        "Furniture": ["Chairs", "Tables", "Storage"],
        "Office Supplies": ["Paper", "Binders", "Art"]
    }
    brands = ["BrandA","BrandB","BrandC"]
    products = []
    for i in range(n_products):
        cat = random.choice(categories)
        products.append([
            f"{prefix}P{2000+i}", cat, random.choice(subcats[cat]), random.choice(brands),
            round(random.uniform(20,200),2)
        ])
    products = pd.DataFrame(products, columns=["product_id","category","subcategory","brand","cost_price"])
    
    # Orders
    start_date = datetime(2024,1,1)
    end_date = datetime(2024,6,30)
    channels = ["Store","Website","Mobile App","Social Media","Marketplace"]
    payments = ["Card","Cash","UPI","NetBanking"]
    def random_date(start, end):
        return start + timedelta(seconds=random.randint(0,int((end-start).total_seconds())))
    
    orders = []
    for i in range(n_orders):
        cid = random.choice(customers.customer_id.tolist())
        odate = random_date(start_date,end_date)
        orders.append([
            f"{prefix}O{3000+i}", odate.date(), cid, 
            random.choice(channels), random.choice(payments),
            random.choice(regions)
        ])
    orders = pd.DataFrame(orders, columns=["order_id","order_date","customer_id","channel","payment_type","region"])
    
    # Order items
    order_items = []
    for oid in orders.order_id:
        for _ in range(random.randint(1,3)):
            pid = random.choice(products.product_id.tolist())
            qty = random.randint(1,5)
            price = round(random.uniform(50,500),2)
            discount = round(random.uniform(0, price*0.2),2)
            order_items.append([oid,pid,qty,price,discount])
    order_items = pd.DataFrame(order_items, columns=["order_id","product_id","qty","item_price","discount"])
    
    # Returns
    returned = np.random.choice(orders.order_id, size=int(0.1*len(orders)), replace=False)
    returns = pd.DataFrame({
        "order_id": returned,
        "return_reason": np.random.choice(["Damaged","Wrong Item","Quality Issue"], size=len(returned))
    })
    
    # Campaigns
    campaign_types = ["Email","SMS","Ads"]
    campaigns = []
    for cid in customers.customer_id:
        if random.random()<0.6:
            campaigns.append([cid, random.choice(campaign_types), np.random.choice([0,1], p=[0.4,0.6])])
        else:
            campaigns.append([cid, random.choice(campaign_types), 0])
    campaigns = pd.DataFrame(campaigns, columns=["customer_id","campaign_type","response"])
    
    # Save CSVs
    base = os.path.join(out_dir, prefix)
    customers.to_csv(f"{base}_customers.csv",index=False)
    products.to_csv(f"{base}_products.csv",index=False)
    orders.to_csv(f"{base}_orders.csv",index=False)
    order_items.to_csv(f"{base}_order_items.csv",index=False)
    returns.to_csv(f"{base}_returns.csv",index=False)
    campaigns.to_csv(f"{base}_campaigns.csv",index=False)

# Output directory
out_dir = "retail_datasets"
os.makedirs(out_dir, exist_ok=True)

# Generate both small and large datasets
generate_dataset(**sizes["small"], prefix="small", out_dir=out_dir)
generate_dataset(**sizes["large"], prefix="large", out_dir=out_dir)

# Create ZIP
shutil.make_archive("retail_datasets", 'zip', out_dir)

print("✅ retail_datasets.zip created with small & large datasets!")
