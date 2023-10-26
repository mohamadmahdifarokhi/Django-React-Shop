import {Link} from "react-router-dom"
import {useEffect, useState} from "react";
import CartLoader from "../product/CartLoader";
import ProductCard from "../product/ProductCard";


export default function ProductsArrival({
                                            data
                                        }) {

    const [loading, setLoading] = useState(true)


    const sleep = ms => new Promise(
        resolve => setTimeout(resolve, ms)
    );

    useEffect(() => {
        async function fetchData() {
            setLoading(true)
            await sleep(3000);
            setLoading(false)
        }

        fetchData();
    }, [])
    return (
        <div className="bg-white">
            <div className="max-w-2xl mx-auto mt-12 py-16 px-4 sm:py-24 sm:px-6 lg:max-w-7xl lg:px-8">
                <h2 className="text-2xl font-extrabold tracking-tight text-gray-900">NEW</h2>

                <div className="mt-6 grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
                    {data &&
                        data !== null &&
                        data !== undefined &&
                        data.map((product) => (
                            <>
                                {loading ? <CartLoader/> : <div key={product.id} className="group relative">
                                    <div
                                        className="shadow-xl p-5 w-full min-h-80 aspect-w-1 aspect-h-1 rounded-md overflow-hidden group-hover:opacity-75">
                                        <img
                                            src={product.photo}
                                            alt=""
                                            className="w-full h-full object-center object-cover lg:w-full lg:h-full"
                                        />
                                    </div>
                                    <div className="mt-4 flex justify-between">
                                        <div>
                                            <h3 className="text-sm text-gray-700">
                                                <Link to={`product/${product.id}`}>
                                                    <span aria-hidden="true" className="absolute inset-0"/>
                                                    {product.name}
                                                </Link>
                                            </h3>

                                        </div>
                                        <p className="text-sm font-medium text-gray-900">${product.price}</p>
                                    </div>
                                </div>}
                            </>

                        ))}
                </div>
            </div>
        </div>
    )
}
  