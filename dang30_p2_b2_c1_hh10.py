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


def bt_dang30_p2_b2_c1_hh10(self):
    # Khai báo biến
    # Phần b
    a_b = random.randint(40, 60)
    B_b = random.choice([60, 65, 70])
    C_b = random.choice([40, 45, 50])
    A_b = 180 - B_b - C_b
    R_b_exact = a_b / (2 * math.sin(math.radians(A_b)))
    R_b_round = round(R_b_exact, 1)
    R_b_str = str(R_b_round).replace('.', ',')
    R_b_false_str = str(round(R_b_exact + random.choice([2.5, -1.5, 1.8]), 1)).replace('.', ',')

    # Phần c (Chọn A=30 độ để sinA = 1/2, a = R cho số đẹp giống đề gốc)
    R_c = random.choice([10, 12, 14, 16])
    a_c = R_c
    A_c = 30
    B_c = random.choice([70, 80, 85])
    C_c_real = 180 - A_c - B_c
    C_c_false = C_c_real - random.choice([10, 15, 20])

    # Phần d
    R_d = random.choice([1, 2, 3])
    A_d = random.choice([45, 60])
    B_d = random.choice([75, 45])
    if A_d == 45 and B_d == 45: 
        B_d = 75
    C_d = 180 - A_d - B_d

    a_d_exact = 2 * R_d * math.sin(math.radians(A_d))
    c_d_exact = 2 * R_d * math.sin(math.radians(C_d))

    a_d_str = str(round(a_d_exact, 2)).replace('.', ',')
    c_d_str = str(round(c_d_exact, 2)).replace('.', ',')

    a_d_false_str = str(round(a_d_exact + 0.5, 2)).replace('.', ',')
    c_d_false_str = str(round(c_d_exact - 0.3, 2)).replace('.', ',')

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho $\\Delta ABC$ có $BC=a, CA=b, AB=c$ và bán kính đường tròn ngoại tiếp $%s$.'''                  
                     %('R'
                         ))

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True $\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C} = 2R$'
    nb_da_1_s = '$\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C} = R$'
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Theo định lí sin trong tam giác, ta có công thức đúng là $\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C} = 2R$.'''
                )

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ########################################################################
    # Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True Nếu $a = %s$ cm, $B = %s^\\circ$ và $C = %s^\\circ$ thì bán kính đường tròn ngoại tiếp làm tròn kết quả đến hàng phần mười là: $R = %s$ cm' %(a_b, B_b, C_b, R_b_str)  
    th_da_1_s = 'Nếu $a = %s$ cm, $B = %s^\\circ$ và $C = %s^\\circ$ thì bán kính đường tròn ngoại tiếp làm tròn kết quả đến hàng phần mười là: $R = %s$ cm' %(a_b, B_b, C_b, R_b_false_str)   
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)


    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Ta có $\\widehat{A} = 180^\\circ - (\\widehat{B} + \\widehat{C}) = 180^\\circ - (%s^\\circ + %s^\\circ) = %s^\\circ$. \\\\
                       Áp dụng định lí sin, ta có: $\\frac{a}{\\sin A} = 2R \\Rightarrow R = \\frac{a}{2 \\sin A} = \\frac{%s}{2 \\sin %s^\\circ} \\approx %s$ cm.'''       
               %(B_b, C_b, A_b, a_b, A_b, R_b_str
                    ))

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ######################################################################## 
    # Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True Nếu $a = %s, B = %s^\\circ, R = %s$ thì góc $C = %s^\\circ$' %(a_c, B_c, R_c, C_c_real)  
    vd_da_1_s = 'Nếu $a = %s, B = %s^\\circ, R = %s$ thì góc $C = %s^\\circ$' %(a_c, B_c, R_c, C_c_false)  
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Áp dụng định lí sin, ta có: $\\frac{a}{\\sin A} = 2R \\Rightarrow \\sin A = \\frac{a}{2R} = \\frac{%s}{2 \\cdot %s} = \\frac{1}{2}$. \\\\
                       Do đó $\\widehat{A} = 30^\\circ$ hoặc $\\widehat{A} = 150^\\circ$. \\\\
                       Trường hợp $\\widehat{A} = 150^\\circ$ bị loại vì $\\widehat{A} + \\widehat{B} = 150^\\circ + %s^\\circ > 180^\\circ$. \\\\
                       Vậy $\\widehat{A} = 30^\\circ$, suy ra $\\widehat{C} = 180^\\circ - (\\widehat{A} + \\widehat{B}) = 180^\\circ - (30^\\circ + %s^\\circ) = %s^\\circ$.'''  
               %(a_c, R_c, B_c, B_c, C_c_real
                    ))

    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ######################################################################## 
    # Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = '\\True Giả sử tam giác $ABC$ được bạn An đã cắt từ một tấm tôn hình tròn có bán kính $R = %s$ (m). Để tam giác $ABC$ có $A = %s^\\circ, B = %s^\\circ$ thì An phải cắt miếng tôn theo hai dây cung $AB \\approx %s$ (m) và $BC \\approx %s$ (m)' %(R_d, A_d, B_d, c_d_str, a_d_str) 
    vdc_da_1_s = 'Giả sử tam giác $ABC$ được bạn An đã cắt từ một tấm tôn hình tròn có bán kính $R = %s$ (m). Để tam giác $ABC$ có $A = %s^\\circ, B = %s^\\circ$ thì An phải cắt miếng tôn theo hai dây cung $AB \\approx %s$ (m) và $BC \\approx %s$ (m)' %(R_d, A_d, B_d, c_d_false_str, a_d_false_str) 
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Ta có $\\widehat{C} = 180^\\circ - (\\widehat{A} + \\widehat{B}) = 180^\\circ - (%s^\\circ + %s^\\circ) = %s^\\circ$. \\\\
                     Độ dài dây cung $BC$ chính là cạnh $a$ của tam giác, dây cung $AB$ là cạnh $c$. Áp dụng định lí sin: \\\\
                     $BC = a = 2R \\sin A = 2 \\cdot %s \\cdot \\sin %s^\\circ \\approx %s$ (m). \\\\
                     $AB = c = 2R \\sin C = 2 \\cdot %s \\cdot \\sin %s^\\circ \\approx %s$ (m).'''
               %(A_d, B_d, C_d, R_d, A_d, a_d_str, R_d, C_d, c_d_str
                    ))

    # Đưa các lời giải vào danh sách lời giải
    list_vdc_2 = [loigiai_vdc_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vdc)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
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
        '\\begin{ex}\n'+
        str(noidungcauhoi)+ 
        '\n\\choiceTFn \n'
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
        '\\end{ex}\n\\end{minipage}\n\n')
    return content

