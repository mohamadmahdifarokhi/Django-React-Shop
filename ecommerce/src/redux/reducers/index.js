import { combineReducers } from 'redux';
import Auth from './auth';
import Alert from './alert';
import Categories from './categories';
import Products from './products';
import Cart from './cart';
import Shipping from "./shipping";
import Payment from "./payment";
import Coupons from "./coupons";
import Orders from "./orders";
import Profile from "./profile";
import Wishlist from "./wishlist";
import Reviews from "./reviews";
import Address from "./address";

export default combineReducers({
    Auth,
    Alert,
    Categories,
    Products,
    Cart,
    Shipping,
    Payment,
    Coupons,
    Orders,
    Profile,
    Wishlist,
    Reviews,
    Address
})

