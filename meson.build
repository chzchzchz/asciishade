project('asciishade', 'c',
    version: 'dev',
    license: 'Unlicense',
    default_options: [
        'buildtype=plain',
        'c_std=c99',
        'werror=true',
        'warning_level=everything'
    ]
)

add_global_arguments(
    language : 'c'
)

dep_ncurses = dependency('ncurses')
cc          = meson.get_compiler('c')

asciishade_deps = [
    dep_ncurses
]

shared_src = [
    'canvas.c',
    'tools.c'
]

asciishade_src = [
    shared_src,
    'main.c'
]

unittest_driver_src = [
    shared_src,
    'unittest_driver.c'
]

executable('asciishade', asciishade_src,
    dependencies: asciishade_deps,
    install: false
)

executable('unittest_driver', unittest_driver_src,
    install: false
)
