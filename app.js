const express = require('express')
const app = express()

const port = 3000
// app.use(express.static(__dirname + "/vidal"))

app.get('/vidal/:url', (req, res)=>{
    res.sendFile(`/vidal/${req.params.url}`, {root : __dirname})
})

app.listen(port, ()=>{
    console.log(`Server running on port ${port}`)
})