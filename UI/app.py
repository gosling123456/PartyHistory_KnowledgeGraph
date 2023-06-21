# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
import flask
app = Flask(__name__)

from flask import Flask, render_template, request

app = Flask(__name__)
import re
sample = False
#实体词典、关系词典、属性词典

entity_dict = {'南昌起义': '事件', '解放战争时期': '事件', '全国政协第一届全体会议': '事件', '指挥辽沈、淮海、平津三大战役': '事件', '出席中共七届二中全会': '事件', '太平洋战争': '事件', '延安整风运动': '事件', '延安文艺座谈会': '事件', '中共中央政治局扩大会议': '事件', '出席中共六届五中全会': '事件', '中共七届一中全会': '事件', '1921年，经毛泽东、何叔衡介绍，夏明翰加入中国共产党': '事件', '1917年，他考入湖南省立第三甲种工业学校': '事件', '中共六届四中全会': '事件', '中共六大': '事件', '中共中央紧急会议': '事件', '中共五大': '事件', '1922年初加入中国共产党': '事件', '1920年8月加入中国社会主义青年团': '事件', '井冈山根据地的创建': '事件', '参加中国革命互济会': '事件', '组建“中国左翼作家联盟。”': '事件', '加入“民权保障同盟会”': '事件', '出席中国左翼作家联盟成立大会': '事件', '中国自由运动大同盟': '事件', '百团大战': '事件', '出席中共七大': '事件', '直罗镇和东征战役': '事件', '1947年3月加入中国共产党': '事件', '1945年7月参加八路军': '事件', '加入中国共产党旅莫支部': '事件', '1951年3月参加中国人民志愿军赴朝作战': '事件', '万隆会议': '事件', '1938年8月入党': '事件', '党的第四、五、六次全国代表大会上': '事件', '八七会议': '事件', '中共川东临时工作委员会成立': '事件', '忻口会战': '事件', '出席中共六届六中全会': '事件', '平型关战役': '事件', '中共八届十一中全会': '事件', '主持第三届全国人大第一次会议': '事件', '出席中央政治局扩大会议': '事件', '党的三大、四大': '事件', '组织马克思学说研究会': '事件', '旅欧中国少年共产党（翌年改名为中国社会主义青年团旅欧支部）': '事件', '1921年周恩来加入中国共产党八个发起组之一的巴黎共产主义小组': '事件', '1940年7月率部挺进苏北': '事件', '重新加入中国共产党': '事件', '成立工农革命军（不久改称红军）第四军': '事件', '中华苏维埃共和国临时政府': '事件', '红军第一方面军成立': '事件', '1934年10月，毛泽东参加红一方面军长征': '事件', '中共中央政治局在贵州召开扩大会议（即遵义会议）': '事件', '指导建立中国新民主主义青年团': '事件', '参加中共中央书记处工作': '事件', '1951年3月参加中国人民志愿军': '事件', '1952年7月加入中国新民主主义青年团': '事件', '1926年4月，陈铁军加入中国共产党。': '事件', '1924年秋，她考入广东大学文学院预科。求学期间，为追求进步，铁心跟共产党走，她改名铁军。': '事件', '1925年加入中国共产党': '事件', '出席庐山会议': '事件', '出席第二届全国人大第一次会议': '事件', '“五卅”运动': '事件', '192610月在北京汇文中学转党，成为中国共产党员': '事件', '北京南苑农民起义': '事件', '1925年6月加入中国共产主义青年团': '事件', '五四”爱国运动': '事件', '1922年8月加入中国共产党': '事件', '四川平民学社': '事件', '日内瓦会议': '事件', '朝鲜战争': '事件', '出席中央政治局会议': '事件', '出席第一届全国人大第一次会议': '事件', '出席中共八大': '事件', '辛亥革命': '事件', '1927年5月，在大革命遭受严重失败的白色恐怖中，徐特立毅然加入中国共产党': '事件', '1927年8月参加南昌起义': '事件', '创办长沙女子师范学校': '事件', '创办长沙师范学校': '事件', '莫斯科中山大学特别班学习': '事件', '井冈山会师': '事件', '组成工农革命军第四军（后称红四军）': '事件', '成立中国工农红军第一路军（后改称红一军团）': '事件', '湘南起义': '事件', '取得了五斗江、新老七溪岭、龙源口等战斗的胜利': '事件', '1926年11月加入中国共产主义青年团': '事件', '1927年6月转入中国共产党': '事件', '井冈山斗争': '事件', '鲁迅任绍兴中学堂教员兼监学': '事件', '鲁迅参加《新青年》改组': '事件', '组建西北反帝同盟军': '事件', '1924年冬加入中国社会主义青年团': '事件', '1925年春转入中国共产党': '事件', '入黄埔军校第四期学习': '事件', '渭华起义': '事件', '1927年9月，致信台静农，拒绝作为诺贝尔文学奖候选人 ': '事件', '1927年29日，营救进步学生无果愤然辞职': '事件', '“四一二-政变”': '事件', '主持召开中共第七次全国代表大会': '事件', '中共七届三中全会': '事件', '第一届全国人民代表大会第一次会议': '事件', '中华人民共和国建立': '事件', '创办利群书社': '事件', '1921年加入中国共产党': '事件', '创办和主编《中国青年》': '事件', '中共“三大”': '事件', '国民党第一、第二次全国代表大会': '事件', '创建共产主义组织': '事件', '中国共产党第一次全国代表大会': '事件', '1913年，37岁的何叔衡考入湖南省立第一师范讲习班': '事件', '共产党早期组织': '事件', '组织成立了新民学会': '事件', '马日事变': '事件', '组建中共湖南支部': '事件', '海出席中国共产党第一次全国代表大会': '事件', '早年加入同盟会、中华革命党，追随孙中山先生参加革命活动，在革命实践中逐步接受马克思主义': '事件', '1921年1月经李大钊、陈独秀介绍加入上海的中国共产党早期组织': '事件', '中共第五次全国代表大会': '事件', '中共五届一中全会': '事件', '南昌领导武装起义': '事件', '中共中央改组': '事件', '中共六届一中全会': '事件', '领导上海工人第三次武装起义': '事件', '离开上海到中央革命根据地': '事件', '“五卅运动”': '事件', '主持第四届全国人大第一次会议': '事件', '出席中共九届二中全会（庐山会议）': '事件', '出席中共九大': '事件', '出席中共十大': '事件', '十届一中全会': '事件', '九届一中全会': '事件', '加入孙中山领导的革命团体中国同盟会': '事件', '重九起义': '事件', '反对北洋军阀段祺瑞的护法战争': '事件', '反对袁世凯复辟帝制的战争': '事件', '共产国际第七次代表大会': '事件', '成立了共产主义小组': '事件', '出席党的一大': '事件', '党的七大': '事件', '中华苏维埃共和国第二次代表大会': '事件', '五四运动': '事件', '1930年参加鄂豫皖红军': '事件', '1929年参加革命，同年加入中国共产党': '事件', '1934年10月参加长征': '事件', '1933年进入中央革命根据地': '事件', '1931年11月，何叔衡进入中央革命根据地': '事件', '1919年，叶挺投身孙中山领导的三民主主义革命，参加了粤军，同年参加了中国国民党': '事件', '1912年，叶挺考入广州黄埔陆军小学，后进入保定军官学校': '事件', '反抗英军屠杀中国民众的运动': '事件', '创办国民革命军第三军军官教育团': '事件', '北伐革命': '事件', '1922年11月，经张申府、周恩来介绍，加入中国共产党': '事件', '1928年加入中国共产主义青年团': '事件', '1930年5月转入中国共产党': '事件', '1929年参加长汀县农民暴动，加入中国工农红军': '事件', '1945年11月加入中国共产党': '事件', '1944年2月参加新四军': '事件', '1950年10月参加中国人民志愿军': '事件', '950年10月，参加中国人民志愿军赴朝作战': '事件', '东征战役': '事件', '主持中央军事政治学校工作': '事件', '广州起义': '事件', '中共六届二中全会': '事件', '赵世炎': '人物', '彭德怀': '人物', '毛泽东': '人物', '鲁迅': '人物', '左权': '人物', '周恩来': '人物', '夏明翰': '人物', '任弼时': '人物', '郑振铎': '人物', '黄继光': '人物', '董存瑞': '人物', '邱少云': '人物', '许建业': '人物', '徐特立': '人物', '陈铁军': '人物', '周文雍': '人物', '彭雪枫 ': '人物', '肖楚女': '人物', '粟裕': '人物', '谢子长': '人物', '蔡和森': '人物', '陈潭秋': '人物', '董必武': '人物', '彭雪枫': '人物', '叶成焕': '人物', '林伯渠': '人物', '何叔衡': '人物', '瞿秋白': '人物', '叶挺': '人物', '李大钊': '人物', '朱德': '人物', '陈毅': '人物', '杨成武': '人物', '杨根思': '人物', '刘志丹': '人物', '恽代英': '人物', '军垦屯田政策': '政策', '黄埔军校': '毕业学校', '邻水县立中学': '毕业学校', '陆军第十六混成旅军官子弟学校': '毕业学校', '东京早稻田大学': '毕业学校', '云南陆军讲武堂': '毕业学校'}
rel_dict = {'参与':'关系','好友':'关系'}
prop_dict = {'出生时间':'属性','出生地点':'属性','原名':'属性','号':'属性','字':'属性','官职':'属性','官职任命时间':'属性','思想内容':'属性','思想时间':'属性','政策提出时间':'属性','政策背景':'属性','毕业时间':'属性','民族':'属性','笔名':'属性','著作内容':'属性','著作地点':'属性','著作时间':'属性','评价':'属性','逝世地点':'属性','逝世年龄':'属性','逝世时间':'属性','发生时间':'属性','毕业学校':'属性','担任':'属性','任':'属性'}

# q = '从出生时间、出生地点、参与事件，评价介绍一下毛泽东'

def ChatWithRobot(q):
    # 模糊查询
    # q='从出生时间、参与战役、官职、著作来介绍一下朱德？'
    time = ['出生时间','出生日期','啥时候出生','破壳日','出生日期','生日']
    for i in time:
        if i in q:
            # print(i)
            q = q.replace(i,'出生时间')
    place = ['出生地点','哪儿出生','出生在哪','什么地方出生','出生在什么地方','啥地方出生','出生在啥地方','那个地方出生','出生在哪地方','在哪儿出生']
    for i in place:
        if i in q:
            # print(i)
            q = q.replace(i,'出生地点')
    participate = ['参与','参加','干了','做什么','干啥']
    for i in participate:
        if i in q:
            # print(i)
            q = q.replace(i,'参与')
    takeplace = ['发生时间','事件时间','啥时候发生的']
    for i in takeplace:
        if i in q:
            # print(i)
            q = q.replace(i,'发生时间')
    graduate = ['毕业学校','毕业院校','从哪儿毕业','毕业于','学成于']
    for i in graduate:
        if i in q:
            # print(i)
            q = q.replace(i,'毕业学校')
    position = ['任','官职','担任']
    for i in position:
        if i in q:
            q = q.replace(i,'任')

    """
    思路：采用正向最大匹配法，分别在实体词典、关系词典、属性词典中进行匹配
    @param q:查询
    @param obj_dict:进行匹配的词典
    """
    def get_kwords(obj_dict,q):
        max_len=5 #每次用于匹配的字符串的最大长度
        word_list=[]#保存匹配得到的词
        start=0 #用于匹配的字符串的起始位置
        while(start<len(q)):#当用于抽取词的句子长度大于0
            #print("当前的start:",start)
            end_cut_pos=min(start+max_len,len(q))
            current_s=q[start:end_cut_pos] #当前用于抽取词的子串
            #print("外current_s:",current_s)
            is_cut_words=False
            for i in range(end_cut_pos-start):
                current_s=q[start:end_cut_pos]
                #print("内current_s",current_s[start:end_cut_pos])
                if current_s in list(obj_dict.keys()):
                    word_list.append((current_s,start,end_cut_pos,obj_dict[current_s])) #保存格式为(匹配到的词，词的起始位置，词的最末位置
                    #print("内current_s",current_s[start:end_cut_pos])
                    start=end_cut_pos
                    #print("jljkljkl",start,q[start])
                    is_cut_words=True
                    break
                else:
                    end_cut_pos=end_cut_pos-1
                    #print("end_cut_pos:",end_cut_pos)
            if is_cut_words==False:
                start=start+1
        return word_list
    # 分别与各个词典进行匹配
    entity_list = get_kwords(entity_dict,q)
    # print("entity_list:",entity_list)
    rel_list=get_kwords(rel_dict,q)
    # print("rel_list:",rel_list)
    prop_list=get_kwords(prop_dict,q)
    # print("prop_list:",prop_list)
    #将匹配得到的所有词保存到obj_list
    obj_list=entity_list+rel_list+prop_list
    #按指定元素进行排序,下面为样例
    # random = [('c', 'Beijing'), ('g', 'Shanghai'), ('a', 'Guangzhou'), ('h', 'Xiamen')]
    # random = sorted(random , key=lambda x: x[1])
    #将匹配到的词按该词在查询中的起始位置进行进行排序
    obj_list = sorted(obj_list , key=lambda x: x[1])
    # print("obj_list:",obj_list)
    # print(q)

    from py2neo import Graph,Node,Relationship
    # Graph()中第一个为local host链接，auth为认证，包含 username 和 password
    g = Graph('http://localhost:7474', auth = ('neo4j', 'gsl1234567890'))
    rules={
        '1':'人物的属性是什么？',      # （距离为1） eg:李大钊的毕业院校   ---------2个实体
        '2':'人物的属性的属性是什么',  # （距离为2） eg:朱德参与南昌起义的事件时间？--------3个实体
        '3':'人物和人物的关系是什么？',# （推理得来） eg:毛泽东和朱德有什么关系 -----2个实体，1个关系
        '4':'人物的关系的属性的属性是什么',  # （距离为3）eg:何叔衡好友参加的事件及事件时间 -------4个实体
        '5':'从属性和属性和属性方面介绍一下人物' # 综合查询, ----------------------关键词介绍
    }

    # cypher_strs =  ["match (n:`人物` {name:'%s'})-[r:`%s`]->(n1) return n1.name",
    #                 "MATCH (n1:`人物` {name:'%s'})-[r1:`参与`]->(n2:`事件` {name:'%s'})-[r2:%s]->(n3) return n3.name",
    #                 "match (n:`人物` {name:'%s'})-[r:`参与`]->(n1) return n1.name",
    #                 "match (n1:`人物` {name:'%s'})-[r1:`%s`]->(n2) match (n2)-[r2:`%s`]->(n3)-[r3:`%s`]->(n4) return n3.name+'发生于'+n4.name",
    #                 "MATCH (n:`人物` {name:'%s'})-[r:%s]->(n1) RETURN n1.name"
    #
    #
    #
    # ]
    def one(name,prop):
        cypher=  "match (n:`人物` {name:'%s'})-[r:`%s`]->(n1) return n1.name"%(name,prop)
        answer = g.run(cypher)
        return answer.data()[0]['n1.name']


    def two(name,event,prop2):
        cypher = "MATCH (n1:`人物` {name:'%s'})-[r1:`参与`]->(n2:`事件` {name:'%s'})-[r2:%s]->(n3) return n3.name"%(name,event,prop2)
        answer = g.run(cypher)
        return answer.data()[0]['n3.name']


    def three(name1,name2):
        def infer(person):
            cypher = "match (n:`人物` {name:'%s'})-[r:`参与`]->(n1) return n1.name" % person
            # 交集
            result = g.run(cypher)
            # 将查询结果转换为列表
            a = [record[0] for record in result]
            return a

        a = infer(name1)
        b = infer(name2)
        inter = list(set(a).intersection(set(b)))
        result = ''
        for i in inter:
            result += i+'、'
        if inter:
            answer = '好友。他们共同参与了%s'%result
        else:
            answer = '不好意思，在所给文本中未查询到二人的关系'
        return answer

    def four(name,relation,prop1,prop2):
        cypher = "match (n1:`人物` {name:'%s'})-[r1:`%s`]->(n2) match (n2)-[r2:`%s`]->(n3)-[r3:`%s`]->(n4) return n3.name+'发生于'+n4.name"%(name,relation,prop1,prop2)
        answer = ''
        for i in g.run(cypher).data():
            answer += i["n3.name+'发生于'+n4.name"]+'\n'

        return answer


    def five(prop_list,entity_list):
        props = [i[0] for i in prop_list]
        # print(props)
        answers = []

        for i in props:
            cypher = "MATCH (n:`人物` {name:'%s'})-[r:%s]->(n1) RETURN n1.name"%(entity_list[0][0],i)
            answers += [{'n1.name':i}] + g.run(cypher).data()
            answer = ''
        for i in answers:
            answer += i['n1.name']+'、'
        return entity_list[0][0]+answer

    # print('entity_list',entity_list)
    # print("rel_list:",rel_list)
    # print("prop_list:",prop_list)
    # print('obj_list',obj_list)
    # print(len(obj_list))

    result = ''
    if '介绍' in q:
        result = five(prop_list+rel_list,entity_list)
    elif len(entity_list) == 1 and len(prop_list) == 1 and len(obj_list)==2:
        result = one(obj_list[0][0],obj_list[1][0])
    elif len(obj_list) == 3:
        result = two(entity_list[0][0],entity_list[1][0],'发生时间')
    elif '关系' in q:
        result = three(entity_list[0][0],entity_list[1][0])
    elif len(obj_list) == 4:
        result = four(obj_list[0][0],obj_list[1][0],obj_list[2][0],obj_list[3][0])
    if result:
        return result
    else:
        return '对不起，党宝查询了大量资料发现所给文本中无相关信息'

@app.route('/g', methods=['GET', 'POST'])
def index():
    return render_template('chat.1.html')


@app.route('/chat.3.html', methods=['GET', 'POST'])
def send():
    message = request.form.get('message')
    message = ChatWithRobot(message)
    return render_template('chat.3.html', key=message)


@app.route('/chat.1.html', methods=['GET', 'POST'])
def eta():
    return render_template('chat.1.html')


@app.route('/')
def hello_world():
    return render_template("login.html")


@app.route('/g')
def hello_world1():
    return render_template("gallery.html")


@app.route('/t')
def page2():  # put application's code here
    return render_template("1.html")


@app.route('/person')
def page3():  # put application's code here
    return render_template("person.html")


@app.route("/chat", methods=["POST", "GET"])
def chat():
    question = request.args.get("question", "")
    question = str(question).strip()
    print(question)
    if question:
        def stream():
            answer = ChatWithRobot(question)
            for data in answer + '&':
                if data == '&':
                    data = "[DONE]"
                print(data)
                yield 'data: %s\n\n' % data

        return flask.Response(stream(), mimetype='text/event-stream')
    return "无内容"


@app.route('/postdata', methods=['POST'])
def postdata():
    data = request.get_json()['data']
    # 处理数据的代码
    response_data = '处理结果'
    return response_data


if __name__ == '__main__':
    app.run()
