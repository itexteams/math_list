import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang17_p2_b1_c1_ds10(self):
    # Khai báo biến
    # Tạo các tham số ngẫu nhiên
    # Câu a: Random chọn định nghĩa đúng/sai
    is_correct_a = random.choice([True, False])
    # Câu b: Random phương trình bậc nhất
    k = random.randint(2, 5)
    c = random.randint(1, 9)
    # Câu c: Số nguyên tố
    limit = random.choice([10, 15, 20])
    primes = [p for p in range(2, limit) if isprime(p)]
    primes_str = "; ".join(map(str, primes))
    # Câu d: Phương trình bậc hai
    r1 = random.randint(-5, -1)
    r2 = random.randint(1, 5)
    b = -(r1 + r2)
    c_quad = r1 * r2

    # Nội dung câu hỏi
    noidungcauhoi = ('Các câu sau là đúng hay sai?')

    ########################################################################
    # Nhận biết - Câu a: Số tự nhiên lẻ/chẵn
    if is_correct_a:
        nb_da_1_d = '\\True Tập hợp các số tự nhiên lẻ là $A = \\{x | x = 2n + 1, n \\in \\mathbb{N}\\}$'
        nb_da_1_s = 'Tập hợp các số tự nhiên lẻ là $A = \\{x | x = 2n, n \\in \\mathbb{N}\\}$'
        loigiai_nb_1 = ('Số tự nhiên lẻ có dạng $2n + 1$ với $n \\in \\mathbb{N}$. Vậy khẳng định là đúng.')
    else:
        nb_da_1_d = '\\True Tập hợp các số tự nhiên chẵn là $A = \\{x | x = 2n, n \\in \\mathbb{N}\\}$'
        nb_da_1_s = 'Tập hợp các số tự nhiên chẵn là $A = \\{x | x = 2n + 1, n \\in \\mathbb{N}\\}$'
        loigiai_nb_1 = ('Số tự nhiên chẵn có dạng $2n$ với $n \\in \\mathbb{N}$. Vậy khẳng định là đúng.')

    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    ########################################################################
    # Thông hiểu - Câu b: Phương trình và miền nghiệm (R vs Z)
    th_da_1_d = '\\True Tập hợp các nghiệm của phương trình $x + %d y = %d$ là $B = \\{(x;y) | x, y \\in \\mathbb{R}, x + %d y = %d\\}$' % (k, c, k, c)
    th_da_1_s = 'Tập hợp các nghiệm của phương trình $x + %d y = %d$ là $B = \\{(x;y) | x, y \\in \\mathbb{Z}, x + %d y = %d\\}$' % (k, c, k, c)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    loigiai_th_1 = ('Tập hợp nghiệm tổng quát của phương trình bậc nhất hai ẩn $x + %d y = %d$ là trên tập số thực $\\mathbb{R}$, không phải tập số nguyên $\\mathbb{Z}$.' % (k, c))

    ########################################################################
    # Vận dụng - Câu c: Số nguyên tố
    vd_da_1_d = '\\True Tập hợp các số nguyên tố nhỏ hơn %d là $C = \\{%s\\}$' % (limit, primes_str)
    vd_da_1_s = 'Tập hợp các số nguyên tố nhỏ hơn %d là $C = \\{%s; %d\\}$' % (limit, primes_str, limit + 1)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    loigiai_vd_1 = ('Liệt kê các số nguyên tố nhỏ hơn %d ta được tập hợp $C = \\{%s\\}$.' % (limit, primes_str))

    ########################################################################
    # Vận dụng cao - Câu d: Phương trình bậc hai
    vdc_da_1_d = '\\True Tập hợp các nghiệm của phương trình $x^2 + %d x + %d = 0$ là $D = \\{%d; %d\\}$' % (b, c_quad, r1, r2)
    vdc_da_1_s = 'Tập hợp các nghiệm của phương trình $x^2 + %d x + %d = 0$ là $D = \\{%d; %d\\}$' % (b, c_quad, r1 + 1, r2 + 1)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    loigiai_vdc_1 = ('Ta có $x^2 + %d x + %d = 0 \\Leftrightarrow (x - %d)(x - %d) = 0 \\Leftrightarrow x = %d$ hoặc $x = %d$. Vậy tập nghiệm $D = \\{%d; %d\\}$.' % (b, c_quad, r1, r2, r1, r2, r1, r2))

    ########################################################################
    # Logic xử lý
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Kết hợp
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    combined_nb = list(zip(list_nb_1, [loigiai_nb_1]))
    combined_th = list(zip(list_th_1, [loigiai_th_1]))
    combined_vd = list(zip(list_vd_1, [loigiai_vd_1]))
    combined_vdc = list(zip(list_vdc_1, [loigiai_vdc_1]))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+
        str(noidungcauhoi)+ '\n'
        '\\choiceTFn \n'
        '{'+str(shuffled_answers_nb[0])+'}\n'
        '{'+str(shuffled_answers_th[0])+'}\n'
        '{'+str(shuffled_answers_vd[0])+'}\n'
        '{'+str(shuffled_answers_vdc[0])+'}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('- -', '+').replace('+ -', '-').replace('+ 1 x', '+x').replace('- 1 x', '-x')
    return content

