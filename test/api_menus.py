# coding:utf8
menu = dict()
menu = [{
    "id": "1",
    "text": "系统管理",
    "state": "open",
    "children": [{
        "id": "11",
        "text": "菜单维护",
        "checked": "true",
        "attributes": {
            "url": "/api_datagrid?id=11"
        }
    }, {
        "id": "12",
        "text": "用户维护",
        "checked": "true",
        "attributes": {
            "url": "/api_datagrid?id=12"
        }
    }, {
        "id": "13",
        "text": "部门维护",
        "checked": "true",
        "attributes": {
            "url": "/api_datagrid?id=13"
        }
    }]
}, {
    "id": "2",
    "text": "权限管理",
    "state": "closed",
    "children": [{
        "id": "21",
        "text": "菜单维护",
        "checked": "true",
        "attributes": {
            "url": "/api_datagrid?id=21"
        }
    }, {
        "id": "22",
        "text": "用户维护",
        "checked": "true",
        "attributes": {
            "url": "/api_datagrid?id=22"
        }
    }, {
        "id": "23",
        "text": "部门维护",
        "checked": "true",
        "attributes": {
            "url": "/api_datagrid?id=23"
        }
    }]
}]
