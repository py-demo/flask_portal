/**
 * Created by saturn on 2018/1/3.
 */

function searchEv() {
  var key = mini.get("keyword").getValue();
  if (key === "" || typeof(key) === undefined) key = "null";
  var node = tree.getSelectedNode();

  if (node) {
    grid.load({account: key, "office.id": node.id});
  } else {
    mini.alert("请先选中一个部门！");
  }
}

function searchKey(ev) {
  if (ev.keyCode === 13) {
    var key = mini.get("keyword").getValue();
    if (key === "" || typeof(key) === undefined) key = "null";
    var node = tree.getSelectedNode();

    if (node) {
      grid.load({account: key, "office.id": node.id});
    } else {
      mini.alert("请先选中一个部门！");
    }
  }
}