import banner from '../../img/banner.png';
import {NavLink} from "react-router-dom";

export default function Example() {
    return (
        <div className="relative bg-white overflow-hidden">
            <div className="pt-16 pb-80 sm:pt-24 sm:pb-40 lg:pt-40 lg:pb-48	h-max">
                <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 sm:static">
                    <div className="sm:max-w-lg">
                        <h1 className="text-4xl font font-extrabold tracking-tight text-black sm:text-6xl lg:-translate-x-40">
                            Mti Pc
                        </h1>
                        <p className="mt-4 text-xl text-black">
                            The best computer parts at the best price
                        </p>
                    </div>
                    <div>
                        <div className="mt-10">
                            <div
                                aria-hidden="true"
                                className="pointer-events-none lg:-translate-y-1/2"
                            >
                                <div
                                    className="absolute transform sm:left-1/2 sm:top-0 sm:translate-x-8 lg:left-1/2 lg:top-1/2 lg:-translate-y-1/2 lg:translate-x-40"
                                    >

                                    <div
                                        className="rounded-lg overflow-hidden sm:opacity-0 lg:opacity-100">
                                        <img
                                            src={banner}
                                            alt=""
                                            className="w-96 h-96"

                                        />
                                    </div>

                                </div>
                            </div>

                            <NavLink
                                to="/shop"
                                className="inline-block text-center bg-indigo-600 border border-transparent rounded-md py-3 px-8 font-medium text-white hover:bg-indigo-700"
                            >
                                Start
                            </NavLink>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
