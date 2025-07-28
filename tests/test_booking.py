from models.booking import CreateBookingResponse
from src.constant import BookingData


def test_create_booking(created_booking):
    try:
        parsed = CreateBookingResponse(**created_booking)

    except Exception as e:
        raise AssertionError(f"Структура ответап не соотвествует: {e}")

    assert parsed.booking.bookingdates.checkin == "2026-01-01"


    assert created_booking['booking']['firstname'] == BookingData.FIRSTNAME.value, (
        "Вернулось некорректное имя\n"
        f"Response:\n{created_booking['booking']['firstname']}\n"
        f"Ожидаемое имя: {BookingData.FIRSTNAME.value}"
    )
    assert created_booking['booking']['lastname'] == BookingData.LASTNAME.value, (
        "Вернулось некорректное фамилия\n"
        f"Response:\n{created_booking['booking']['lastname']}\n"
        f"Ожидаемое фамилия: {BookingData.LASTNAME.value}"
    )


def test_update_booking(get_token, headers, created_booking, booking_client, update_booking_payload):
    headers.update({'Accept': 'application/json'})
    headers.update({'Cookie': f'token={get_token}'})
    booking_id = created_booking['bookingid']
    response = booking_client.update_booking(update_booking_payload.build(),headers,booking_id)
    print()
    print()
    print(response.json())