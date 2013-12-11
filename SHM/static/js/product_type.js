var product_type = 
{
    'd' : ['bike', 'moto', 'e-moto'],
    'b' : ['bkjc',
        'kysj',
        'gre',
        'tofel',
        'rwkx',
        'zrkx'],
    'e' : ['desktop',
        'laptop',
        'screen',
        'crate',
        'keyboard',
        'came',
        'phone',
        ],
    'c' : ['clothe',
        'bottoms',
        'shoes',
        'decoration'],
    'm' : ['gita',
        'album',
        'dizi'],
    'l' : ['lamp',
        'desk',
        'hanger',
        'gym',
        'big_ball',
        'small_ball',
        'elec',],
    'h' : ['one',
    'one-one',
    'two-one',
    'two-two',
    'two-three',
    'three-one',
    'three-two',
    'three-three',
    'bigger'],
    'o' : ['o'],
};
var key_value = {
    'd' : '代步', 
    'bike' : '自行车', 'moto' : '摩托车', 'e-moto' : '电动车', 
    'b' : '书籍',
    'bkjc' : '本科书籍', 'kysj' : '考研书籍', 'gre' : 'GRE', 'tofel' : '托福', 'rwkx' : '人文科学', 'zrkx' : '自然科学',
    'e' : '数码',
    'desktop' : '台式机整机', 'laptop' : '笔记本', 'screen' : '显示器', 'crate' : '机箱', 'keyboard' : '键盘', 'came' : '照相机', 'phone' : '电话', 
    'c' : '服装',
    'clothe' : '上装', 'bottoms' : '下装', 'shoes' : '鞋', 'decoration' : '饰物',
    'm' : '音乐',
    'gita' : '吉他', 'dizi' : '笛子', 'album' : '专辑',
    'l' : '生活用品',
    'lamp' : '台灯', 'desk' : '桌子', 'hanger' : '衣架', 'gym' : '健身相关', 'big_ball' : '大球运动', 'small_ball' : '小球运动', 'elec': '家用电器',
    'h' : '住房',
    'one' : '单间','one-one' : '一室一厅', 'two-one' : '两室一厅', 'two-two' : '两室两厅', 'two-three' : '两室三厅','three-one' : '三室一厅', 'three-two' : '三室两厅', 'three-three' : '三室三厅', 'bigger' : '很大的房子',
    'o' : '其他',
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
