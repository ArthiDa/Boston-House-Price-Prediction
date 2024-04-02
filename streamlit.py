import streamlit as st
from app import predict


# 8.3252,41.,6.98412698, 1.02380952,322., 2.55555556, 37.88, -122.23


def main():
    data = []
    st.title("Boston House Price Prediction")
    st.write("Please Enter the Following Details to Predict the House Price")
    medInc = st.number_input("Enter Median Income", help="e.g. 8.32")
    data.append(medInc)
    avgHouseAge = st.number_input("Enter House Age", help="e.g. 41.00")
    data.append(avgHouseAge)
    avgRooms = st.number_input("Enter Average Number of Rooms", help="e.g. 6.98")
    data.append(avgRooms)
    avgBedrooms = st.number_input("Enter Average Number of Bedrooms", help="e.g. 1.02")
    data.append(avgBedrooms)
    population = st.number_input("Enter Population", help="e.g. 322.00")
    data.append(population)
    avgFamilies = st.number_input("Enter Average Number of Families", help="e.g. 2.56")
    data.append(avgFamilies)
    latitude = st.number_input("Enter Latitude", help="e.g. 37.88")
    data.append(latitude)
    longitude = st.number_input("Enter Longitude", help="e.g. -122.23")
    data.append(longitude)

    if st.button("Predict"):
        prediction = predict(data)
        st.success(
            f"The House Price Prediction is {prediction:.2f} hundreds of thousands of dollars"
        )


if __name__ == "__main__":
    main()
