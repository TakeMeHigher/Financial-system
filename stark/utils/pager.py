class Pagination(object):
    def __init__(self, current_page, totalCount, base_url,parmas, per_page_count=10, max_page_count=11):
        try:
            current_page = int(current_page)
        except:
            current_page = 1
        if current_page < 1:
            current_page = 1
        # 当前页
        self.current_page = current_page
        # 总记录数/总条数
        self.totalCount = totalCount
        # 每页显示的数量
        self.per_page_count = per_page_count

        max_page_num, v = divmod(totalCount, per_page_count)
        if v:
            max_page_num += 1

        # 总页数
        self.max_page_num = max_page_num
        # 显示页码的个数
        # 页面上默认显示11个页面（当前页在中间）
        self.max_page_count = max_page_count

        self.half_page_count = int((self.max_page_count - 1) / 2)
        # URL前缀
        self.base_url = base_url

        import copy
        parmas=copy.deepcopy(parmas)
        print(parmas,'------******')
        self.parmas=parmas
    # 每页开始的记录
    @property
    def start(self):
        return (self.current_page - 1) * self.per_page_count

    # 每页结束的记录
    @property
    def end(self):
        return self.per_page_count * self.current_page

    # 页码显示
    def page_html(self):

        if self.max_page_num < self.max_page_count:
            page_start = 1
            page_end = self.max_page_num
        else:
            if self.current_page < self.half_page_count:
                page_start = 1
                page_end = self.max_page_count

            else:
                if (self.current_page + self.half_page_count) > self.max_page_num:
                    page_start = self.max_page_num - self.max_page_count + 1
                    page_end = self.max_page_num

                else:
                    page_start = self.current_page - self.half_page_count
                    page_end = self.current_page + self.half_page_count

        html_list = []
        # 首页
        self.parmas['page'] = 1
        first_page = '<li><a href="%s?%s">首页</a></li>' % (self.base_url,self.parmas.urlencode())
        html_list.append(first_page)

        # 上一页

        if self.current_page == 1:
            pre_page='<li class="disabled"><a href="#" aria-label="Previous" ><span aria-hidden="true">&laquo;</span></a></li>'
            #pre_page = "<a href='%s?%s' >上一页</a>" % (self.base_url, self.parmas.urlencode())
        else:
            self.parmas['page'] =self.current_page-1
            #pre_page = "<a href='%s?%s'>上一页</a>" % (self.base_url, self.parmas.urlencode())
            pre_page = '<li><a href="%s?%s" aria-label="Previous"><span aria-hidden="true"> &laquo; </span></a> </li>'%(
            self.base_url, self.parmas.urlencode())
        html_list.append(pre_page)


        for i in range(page_start, page_end + 1):
            self.parmas['page'] =i
            if i == self.current_page:
                #tmp = "<a href='%s?%s' class='active'>%s</a>" % (self.base_url, self.parmas.urlencode(), i)
                tmp='<li class="active"><a href="%s?%s" >%s</a></li>'%(self.base_url, self.parmas.urlencode(), i)
            else:
                tmp='<li><a href="%s?%s" >%s</a></li>'%(self.base_url, self.parmas.urlencode(), i)

            html_list.append(tmp)

        # 下一页
        if self.current_page == self.max_page_num:

            #next_page = "<a href='%s?%s'>下一页</a>" % (self.base_url, self.parmas.urlencode())
            next_page='<li class="disabled"><a  aria-label="Next" ><span aria-hidden="true">&raquo;</span></a></li>'
        else:
            self.parmas['page']=self.current_page+1
            #next_page = "<a href='%s?%s'>下一页</a>" % (self.base_url,self.parmas.urlencode())
            next_page= next_page='<li><a href="%s?%s" aria-label="Next" disabled="disabled"><span aria-hidden="true">&raquo;</span></a></li>'% (self.base_url,self.parmas.urlencode())

        html_list.append(next_page)

        self.parmas['page']=self.max_page_num
        last_url = "<li><a href='%s?%s'>尾页</a></li>" % (self.base_url, self.parmas.urlencode())
        html_list.append(last_url)
        return ''.join(html_list)
