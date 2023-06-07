import axios from 'axios';
import {
    GET_SHIPPING_OPTIONS_SUCCESS,
    GET_SHIPPING_OPTIONS_FAIL
} from './types';

export const get_shipping_options = (city) => async dispatch => {
    const config = {
        headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': `JWT ${localStorage.getItem('access')}`
            }
    };

    const body = JSON.stringify({city});


    try {
        const res = await axios.post(`${process.env.REACT_APP_API_URL}/api/shipping/get-shipping-options`,
            body, config);

        if (res.status === 200) {
            dispatch({
                type: GET_SHIPPING_OPTIONS_SUCCESS,
                payload: res.data
            });
        } else {
            dispatch({
                type: GET_SHIPPING_OPTIONS_FAIL
            });
        }
    } catch (err) {
        dispatch({
            type: GET_SHIPPING_OPTIONS_FAIL
        });
    }
};