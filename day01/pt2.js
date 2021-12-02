input = document.body.textContent.split`\n`.reduce((p,c)=>({s:p.l[2]&&-c<p.l.shift()?p.s+1:p.s,l:p.l.concat(-c)}),{s:0,l:[]}).s
