def get_custom_css():
    return """
    <style>
        /* Center the button */
        .stButton > button {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 250px;
            margin: auto;
            padding: 12px;
            background-color: red !important;
            color: white !important;
            font-size: 18px;
            font-weight: bold;
            border-radius: 8px;
            box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.3);
            border: none;
            transition: 0.3s;
            cursor: pointer;
        }

        /* Button hover effect */
        .stButton > button:hover {
            background-color: darkred !important;
            box-shadow: 5px 5px 12px rgba(0, 0, 0, 0.5);
        }

        /* Center warning message */
        .stAlert {
            text-align: center;
        }
    </style>
    """
