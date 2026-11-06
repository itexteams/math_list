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


def bt_dang6_p2_b5_c1_hh11(self):
    # Khai báo các đối tượng/tên hình để random tạo đề bài
    list_tam_giac = ['tam giác', 'tam giác đều', 'tam giác vuông', 'tam giác cân']
    list_hinh_chu_nhat = ['hình chữ nhật', 'hình vuông', 'hình thoi']
    list_hinh_thang = ['ABCD', 'MNPQ', 'EFGH']

    ten_tg = random.choice(list_tam_giac)
    ten_hcn = random.choice(list_hinh_chu_nhat)
    ten_ht = random.choice(list_hinh_thang)

    if ten_ht == 'ABCD':
        day1, day2 = 'AB', 'CD'
        day1_p, day2_p = "A'B'", "C'D'"
    elif ten_ht == 'MNPQ':
        day1, day2 = 'MN', 'PQ'
        day1_p, day2_p = "M'N'", "P'Q'"
    else:
        day1, day2 = 'EF', 'GH'
        day1_p, day2_p = "E'F'", "G'H'"

    # Nội dung câu hỏi
    noidungcauhoi = ('''Xét các nhận định về hình biểu diễn qua phép chiếu song song.''')

    ###################################################################### Nhận biết ######################################################
    # Mệnh đề a: Hình biểu diễn của một tam giác
    nb_da_1_d = '\\True Một %s bất kỳ luôn có thể biểu diễn bằng một tam giác' % (ten_tg)
    nb_da_1_s = 'Hình biểu diễn của một tam giác luôn luôn là một đoạn thẳng'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = ('''Một tam giác (kể cả tam giác đều, tam giác cân hay tam giác vuông) khi mặt phẳng chứa nó không song song với phương chiếu thì hình chiếu song song của nó vẫn là một tam giác. Do đó, một %s bất kỳ có thể biểu diễn bởi một tam giác tuỳ ý.''' % (ten_tg))

    list_nb_2 = [loigiai_nb_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ###################################################################### Thông hiểu ######################################################
    # Mệnh đề b: Hình biểu diễn của hình chữ nhật/hình vuông
    th_da_1_d = '\\True Một %s có thể được biểu diễn bởi một hình bình hành không có góc vuông' % (ten_hcn)
    th_da_1_s = 'Một %s bắt buộc phải được biểu diễn bởi một hình chữ nhật' % (ten_hcn)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    list_th_1 = [th_da_1]

    loigiai_th_1 = ('''Phép chiếu song song nói chung không bảo toàn độ lớn của góc và độ dài đoạn thẳng, chỉ bảo toàn tính song song. Vì vậy, %s (có hai cặp cạnh đối song song) có thể được biểu diễn bởi một hình bình hành không nhất thiết có góc vuông.''' % (ten_hcn))

    list_th_2 = [loigiai_th_1]

    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ###################################################################### Vận dụng ######################################################
    # Mệnh đề c: Hình biểu diễn của hình thang và tỉ số hai đáy
    vd_da_1_s = 'Với hình thang $%s$ có $%s // %s$, khi biểu diễn chỉ cần giữ $%s // %s$, còn tỉ số $\\dfrac{%s}{%s}$ có thể thay đổi tuỳ ý' % (ten_ht, day1, day2, day1_p, day2_p, day1, day2)
    vd_da_1_d = '\\True Với hình thang $%s$ có $%s // %s$, khi biểu diễn phải giữ $%s // %s$ và bảo toàn tỉ số $\\dfrac{%s}{%s}$' % (ten_ht, day1, day2, day1_p, day2_p, day1, day2)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    list_vd_1 = [vd_da_1]

    loigiai_vd_1 = ('''Phép chiếu song song bảo toàn tính song song và bảo toàn tỉ số độ dài của hai đoạn thẳng cùng nằm trên một đường thẳng hoặc trên hai đường thẳng song song. Vì hai đáy $%s // %s$ nên hình biểu diễn phải là hai đoạn thẳng song song $%s // %s$ và phải giữ nguyên tỉ số $\\dfrac{%s}{%s} = \\dfrac{%s}{%s}$. Do đó không thể thay đổi tỉ số này tuỳ ý.''' % (day1, day2, day1_p, day2_p, day1_p, day2_p, day1, day2))

    list_vd_2 = [loigiai_vd_1]

    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ###################################################################### Vận dụng cao ######################################################
    # Mệnh đề d: Hình biểu diễn của hình tròn
    vdc_da_1_s = 'Hình biểu diễn của một hình tròn nhất thiết phải là một hình tròn'
    vdc_da_1_d = '\\True Hình biểu diễn của một hình tròn thường là một hình elip'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    list_vdc_1 = [vdc_da_1]

    loigiai_vdc_1 = ('''Hình biểu diễn qua phép chiếu song song của một hình tròn thường là một hình elip hoặc một đoạn thẳng (khi mặt phẳng chứa hình tròn song song với phương chiếu), không nhất thiết phải là hình tròn.''' )

    list_vdc_2 = [loigiai_vdc_1]

    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
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
    '\\end{ex}\n \\end{minipage}\n\n')
    return content

