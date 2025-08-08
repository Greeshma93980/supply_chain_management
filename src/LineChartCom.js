import React from "react";
import { LineChart,Line,XAxis,YAxis,CartesianGrid,Tooltip,Legend,ResponsiveContainer } from "recharts";
function LineChartCom(){
const data=[
    {date:"2025-09-01",sales:400},
    {date:"2025-08-01",sales:900},
    {date:"2025-07-01",sales:520},
    {date:"2025-06-01",sales:490},
    {date:"2025-05-01",sales:500},
];
    return(
        <ResponsiveContainer width="100%" height={300}>
            <LineChart data={data} margin={{top:20,right:30,left:0,bottom:0}}>
                <CartesianGrid strokeDasharray="3 3"/>
                <XAxis datakey="date"/>
                <YAxis />
                <Tooltip />
                <Legend />
                <Line type="monotone" datakey="sales" stroke="#8884d8"/>
            </LineChart>
        </ResponsiveContainer>
    );
}
export default LineChartCom;