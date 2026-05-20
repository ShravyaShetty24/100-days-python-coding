def restaurant(**customer):
    def show_customer():
        print("\n------FOOD BILL-----\n")
        print("Customer :",customer["name"])
        print("Phone :",customer["phone"])
        print("Place :",customer["place"])
    def generate_bill(*prices):
        total=sum(prices)
        gst=lambda x:x*0.05
        gst_amount=gst(total)
        final_amount=total+gst_amount
        print("\nFood Total : ",total)
        print("GST : ",gst_amount)
        print("Final Amount : ",final_amount)
    def thank_you():
        print("\n Thank You Visit again")
    
    show_customer()
    generate_bill(120,250,80,150,200)
    thank_you()

restaurant(name="Shravya Shetty",phone="1234567891",place="Thirthahalli")    