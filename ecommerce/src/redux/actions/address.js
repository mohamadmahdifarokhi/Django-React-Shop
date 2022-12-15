import axios from 'axios';
import {setAlert} from './alert';
import {
    GET_USER_ADDRESS_SUCCESS,
    GET_USER_ADDRESS_FAIL,
} from './types';


export const get_user_address = (addressId) => async dispatch => {
    if (localStorage.getItem('access')) {
        const config = {
            headers: {
                'Accept': 'application/json',
                'Authorization': `JWT ${localStorage.getItem('access')}`
            }
        };

        const body = JSON.stringify({
            addressId
        });

        try {
            const res = await axios.post(`${process.env.REACT_APP_API_URL}/api/profile/address`, body, config);

            if (res.status === 200) {
                dispatch({
                    type: GET_USER_ADDRESS_SUCCESS,
                    payload: res.data
                });
            } else {
                dispatch({
                    type: GET_USER_ADDRESS_FAIL
                });
            }
        } catch (err) {
            dispatch({
                type: GET_USER_ADDRESS_FAIL
            });
        }
    }
}