import {
    GET_USER_ADDRESS_SUCCESS,
    GET_USER_ADDRESS_FAIL,
} from '../actions/types';

const initialState = {
    address: null
};

export default function Profile(state = initialState, action) {
    const {type, payload} = action;

    switch (type) {
        case GET_USER_ADDRESS_SUCCESS:
            return {
                ...state,
                address: payload.address
            }
        case GET_USER_ADDRESS_FAIL:
            return {
                ...state
            }
        default:
            return state
    }
}