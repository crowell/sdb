{
  "targets": [
    {
      "target_name": "sdb-json",
      "sources": [ "sdb-json.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "../../../src"
      ],
      "libraries": [
        "../../../../src/libsdb.a"
      ]
    }
  ]
}
