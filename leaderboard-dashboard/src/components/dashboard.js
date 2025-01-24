export default function DashBoard(){
    return(
        <div className="bg-black w-[700px] h-[500px] rounded-2xl   ">

                <div className="">
                    <h1 className=" mt-5 text-red-700 text-center text-3xl font-pixel">Leaderboard</h1>

                </div>
                <div className=" items-center  flex flex-col gap-4 mt-[90px] font-serif">
                    <p className="text-red-700 text-xl font-pixel">1.Vnate, problems solved: 70</p>
                    <p className="text-red-700 text-xl font-pixel">2.iOliver678, problem solved: 54</p>
                    <p className="text-red-700 text-xl font-pixel">3.Its_a_Matt, problems solved: 50</p>

                </div>


                <div className=" justify-center flex flex-row gap-4 mt-[109px]  ">
                        <button className="bg-gray-500  text-white font-bold py-2 px-4 rounded font-pixel ">update</button>
                        <button className="bg-gray-500  text-white font-bold py-2 px-4 rounded font-pixel ">top user</button>
                        <button className="bg-gray-500 text-white font-bold py-2 px-4 rounded font-pixel">hour update</button>
                </div>

        </div>
    )
}