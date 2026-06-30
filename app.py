import streamlit as st

# Page settings
st.set_page_config(
    page_title="ExploreX",
    page_icon="🌍",
    layout= "wide"
)

# Sidebar menu
st.sidebar.image(
        "images/logo.png",
        width=180
    )
st.sidebar.markdown("## Navigation")

menu = st.sidebar.selectbox(
    "Select Menu",
    [
        "🏠Home",
        "🌍Explore Destinations",
        "💴Trip Budget Estimator",
        "🛩️Select Your Destination",
        "💼Packing Checklist",
        "ℹ️About Us",
        "📞Contact Support"
    ]
)
st.sidebar.markdown("---")
st.sidebar.markdown("""
*The world is a book,*

*and those who do not*

*travel read only one page.*

""")
st.sidebar.markdown("✈️........")

st.sidebar.caption("-----------------")

# Home Page
if menu == "🏠Home":
    st.title("🌎EploreX")
    st.subheader("World Travel & Exploration System")
    
    st.image(
        "images/World Trip.jpg",
        width=500
    )
    st.markdown("""
        ### 🌟 Popular Destinations
        🌍 Paris, France  
        🏙️ Dubai, UAE  
        🏝️ Maldives  
        🗼 Tokyo, Japan  
        🌴 Bali, Indonesia
        """)

    st.divider()
    st.info(
            """
          ℹ️Welcome to ExploreX, your travel companion for discovering
                amazing destinations around the world.
            """
        )
    st.markdown(
    "✈️ Plan your trips • Explore destinations • Create unforgettable memories"
    )
    st.divider()
    st.success(
        "✨ Every great journey begins with a dream. Start your adventure with ExploreX today!"
    )

# Destinations Page
elif menu == "🌍Explore Destinations":

    st.title("🌎 Explore Destinations")
    st.subheader("Available Destinations")

    # Destination details stored in dictionary
    destinations = {
        "Paris": {
            "country": "France",
            "type": "City",
            "budget": 150000,
            "image": "images/paris.jpg"
        },
        "Dubai": {
            "country": "UAE",
            "type": "Luxury",
            "budget": 120000,
            "image":"images/Dubai.jpg"
        },
        "Maldives": {
            "country": "Maldives",
            "type": "Beach",
            "budget": 180000,
            "image":"images/maldives.jpg"
        },
        "Tokyo": {
            "country": "Japan",
            "type": "City",
            "budget": 200000,
            "image":"images/Japan.jpg"
        },
        "Bali": {
            "country": "Indonesia",
            "type": "Island",
            "budget": 100000,
            "image":"images/bali.jpg"
        }
    }

    # Display all destinations
    for place, details in destinations.items():

        st.subheader(f"📍 {place}")
        st.image(details["image"], width= 400)
        st.write(f"Country : {details['country']}")
        st.write(f"Type : {details['type']}")
        st.write(f"Budget : ₹{details['budget']}")
        st.divider()

    # Trip Budget Estimator
elif menu == "💴Trip Budget Estimator":

    st.title("💰 Trip Budget Estimator")

    st.info(
        "Plan your budget and travel with confidence. ✈️"
    )

    destination = st.selectbox(
        "Choose Yours Destination",
        [
            "Paris",
            "Dubai",
            "Maldives",
            "Tokyo",
            "Bali"
        ]
    )

    travelers = st.number_input(
        "Number of Travelers 👥",
        min_value=1,
        step=1
    )

    days = st.number_input(
        "Trip Duration (Days)",
        min_value=25,
        max_value=30,
        step=1
    )

    destination_cost = {
        "Paris": 150000,
        "Dubai": 120000,
        "Maldives": 180000,
        "Tokyo": 200000,
        "Bali": 100000
    }

    if st.button("Estimate Budget"):

        # Budget depends only on travelers
        total_cost = (
            destination_cost[destination]
            * travelers
        )

        st.subheader("📋 Trip Summary")

        st.info(
            f"""
        📍 Destination: {destination}

        👥 Travelers: {travelers}

        📅 Duration: {days} days

        💰 Budget: ₹{total_cost:,}
        """
        )

        st.caption(
        "🎉 Your trip budget has been calculated successfully. Have a wonderful journey! ✈️"
        )

# Packing Checklist
elif menu == "💼Packing Checklist":

    st.title("🧳 Must Carry Items")

    st.info(
        "Check the important items you should carry before starting your journey."
    )

    destination = st.selectbox(
        "Choose Your Destination",
        [
            "Paris",
            "Dubai",
            "Maldives",
            "Tokyo",
            "Bali"
        ]
    )

    essentials = {
        "Paris": [
            "Passport",
            "Travel Documents",
            "Warm Jacket",
            "Camera",
            "Power Bank",
            "Comfortable Walking Shoes"
        ],

        "Dubai": [
            "Passport",
            "Travel Documents",
            "Sunglasses",
            "Water Bottle",
            "Light Cotton Clothes",
            "Sunscreen"
        ],

        "Maldives": [
            "Passport",
            "Travel Documents",
            "Beach Wear",
            "Mobile Phone",
            "Phone Charger",
            "Sunscreen"
        ],

        "Tokyo": [
            "Passport",
            "Travel Documents",
            "Wallet",
            "Camera",
            "Phone Charger",
            "Shoes",
        ],

        "Bali": [
            "Passport",
            "Travel Documents",
            "Wallet",
            "Mobile Phone",
            "Beach Wear",
            "Mosquito Repellent"
        ]
    }

    if st.button("View Items"):

        st.subheader("🎒Recommended Items")

        for item in essentials[destination]:
            st.write(f"✅ {item}")

        st.success(
            "🎒 Your travel essentials checklist is ready. Have a wonderful journey!"
        )

        st.caption(
            "✈️ Double-check your essentials before you start your adventure."
        )


# Select Your Destination
elif menu == "🛩️Select Your Destination":

    st.title("🗺️ Choose Your Destination")

    destinations = {
    "Paris": {
        "country": "France",
        "type": "City",
        "budget": 150000,
        "image": "images/paris.jpg",
        "places": [
            "Eiffel Tower",
            "Louvre Museum",
            "Notre-Dame Cathedral",
            "Arc de Triomphe"
        ]
    },

    "Dubai": {
        "country": "UAE",
        "type": "Luxury",
        "budget": 120000,
        "image":"images/Dubai.jpg",
        "places": [
            "Burj Khalifa",
            "Dubai Mall",
            "Palm Jumeirah",
            "Desert Safari"
        ]
    },

    "Maldives": {
        "country": "Maldives",
        "type": "Beach",
        "budget": 180000,
        "image":"images/maldives.jpg",
        "places": [
            "Male City",
            "Maafushi Island",
            "Vaadhoo Island",
            "Banana Reef"
        ]
    },

    "Tokyo": {
        "country": "Japan",
        "type": "City",
        "budget": 200000,
        "image":"images/Japan.jpg",
        "places": [
            "Tokyo Tower",
            "Shibuya Crossing",
            "Senso-ji Temple",
            "Mount Fuji"
        ]
    },

    "Bali": {
        "country": "Indonesia",
        "type": "Island",
        "budget": 100000,
        "image":"images/bali.jpg",
        "places": [
            "Ubud",
            "Tanah Lot Temple",
            "Kuta Beach",
            "Tegallalang Rice Terrace"
        ]
    }
}
    place = st.selectbox(
        "Choose Destination",
        list(destinations.keys())
    )
    import os
    st.write(os.path.exists(destinations[place]["image"]))
    
    if "image" in destinations[place]:
        st.image(
            destinations[place]["image"],
            width=500
        )

    st.subheader("Destination Details")

    st.write(f"Country : {destinations[place]['country']}")
    st.write(f"Type : {destinations[place]['type']}")
    st.write(f"Budget : ₹{destinations[place]['budget']}")
    
    st.subheader("*📍Places Covered*")

    for tourist_place in destinations[place]["places"]:
        st.write(f"✅ {tourist_place}")

    if st.button("Select Destination"):

        st.success(
                f"🎉 Your trip to {place} has been selected successfully!"
            )

        st.caption(
            "✨ Get ready to explore new places and create unforgettable memories."
        )

        st.info(
            "💳 Please proceed to the payment process to confirm your booking."
        )

        st.balloons()

# About ExploreX
elif menu == "ℹ️About Us":

    st.subheader("ℹ️ About Us")

    st.markdown("""
    🌍 **Who We Are**
    ExploreX is a travel platform designed to make trip planning simple and enjoyable.

    ✈️ **Our Goal**
    Help travelers discover amazing destinations and create unforgettable memories.

    💙 **What We Offer**
    • Destination exploration
    • Trip budget estimation
    • Packing checklists
    • Easy travel planning

    ✨ **Our Promise**
    Explore more. Dream more. Travel more.
    """)
    st.write(
        """
       *ExploreX is a World Travel & Exploration System designed to help
        travelers discover amazing destinations, estimate trip budgets,
        plan their journeys, and create unforgettable experience.*
        """
    )


elif menu == ("📞Contact Support"):
    
    st.subheader("☎️Customer Support")

    st.write("📧 Email : support@explorex.com")
    st.write("📱 Phone : +91 9876543210")
    st.write("🌐 Website : www.explorex.com")
    st.write("📍 Address : Hyderabad, Telangana, India")

    st.info(
        "Need assistance? Our support team is always ready to help you with your travel plans and answer your questions."
    )

    st.success(
                """
        ✨ Explore the world, one destination at a time!

        Thank you for choosing ExploreX.
        Make your journey beautiful and your memories unforgettable.

        Wishing you safe travels, endless adventures,
        and wonderful experiences ahead! ✈️🌍
        """
    )

    st.caption(
        "Made with ❤️ by the ExploreX Team."
    )
