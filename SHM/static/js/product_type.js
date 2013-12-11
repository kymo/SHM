var product_type = 
{
    'd' : ['bike', 'moto'],
    'b' : ['bkjc',
        'kysj',
        'gre',
        'tofel',
        'rwkx',
        'zrkx'],
    'e' : ['com',
        'came',
        'phone',
        'mp'],
    'c' : ['clothe',
        'bottoms',
        'shoes',
        'decoration'],
    'm' : ['gita',
        'dizi'],
    'l' : ['sf',
        'sdf'],
};
var key_value = {
    'd' : '代步', 
    'bike' : '自行车', 'moto' : '电动车', 
    'b' : '书籍',
    'bkjc' : '本科书籍', 'kysj' : '考研书籍', 'gre' : 'GRE', 'tofel' : '托福', 'rwkx' : '人文科学', 'zrkx' : '自然科学',
    'e' : '数码',
    'com' : '计算机相关', 'came' : '照相机', 'phone' : '电话', 
    'c' : '服装',
    'clothe' : '上装', 'bottoms' : '下装', 'shoes' : '鞋', 'decoration' : '饰物',
    'm' : '音乐',
    'gita' : '吉他', 'dizi' : '笛子',
    'l' : '生活',
    'sf' : 's', 'sdf' : 'sdf'
}

function onchange(first_id ,second_id)
{
    var key = $(first_id).val();
    var values = product_type[key];
    var option_cnt = "";
    for(var value in values)
    {
        
        option_cnt += "<option value = '" + values[value] + "'>" + key_value[values[value]] + "</option>";
    }
    
    $(second_id).html(option_cnt);
}
