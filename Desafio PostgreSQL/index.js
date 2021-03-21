const fs = require('fs')

for(let index = 2742 ; index < 2747; index++){
    let pathName = `Uri-PostgreSQL-${index}.txt`
    fs.writeFileSync(pathName, "")
}

