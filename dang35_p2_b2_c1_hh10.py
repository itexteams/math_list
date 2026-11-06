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


def bt_dang35_p2_b2_c1_hh10(self):
    # Khai báo biến và chọn cấu hình ngẫu nhiên (bộ ba Pytago và hệ số chia cạnh)
    configs = [
        (6, 8, 1, 4),   # Cấu hình gốc: AB=6, AC=8, CD=BE=1/4 BC
        (3, 4, 1, 4),   # AB=3, AC=4, CD=BE=1/4 BC
        (9, 12, 1, 3),  # AB=9, AC=12, CD=BE=1/3 BC
        (12, 16, 1, 4)  # AB=12, AC=16, CD=BE=1/4 BC
    ]
    c_val, b_val, k_num, k_den = random.choice(configs)
    a_val = math.isqrt(c_val**2 + b_val**2)
    k_str = "\\frac{%s}{%s}" % (k_num, k_den) if k_den != 1 else str(k_num)

    # Chuyển đổi sang đối tượng SymPy để tính toán chính xác
    a = sp.Integer(a_val)
    c = sp.Integer(c_val)
    b = sp.Integer(b_val)
    k = sp.Rational(k_num, k_den)

    # Tính toán các cạnh và góc phụ
    BE_exact = k * a
    cos_B = sp.Rational(c, a)
    cos_C = sp.Rational(b, a)

    AE2_exact = c**2 + BE_exact**2 - 2 * c * BE_exact * cos_B
    AD2_exact = b**2 + BE_exact**2 - 2 * b * BE_exact * cos_C
    ED_exact = a - 2 * BE_exact
    ED2_exact = ED_exact**2

    # Tính cos góc EAD và chuyển sang độ để làm tròn
    cos_EAD_exact = sp.simplify((AE2_exact + AD2_exact - ED2_exact) / (2 * sp.sqrt(AE2_exact) * sp.sqrt(AD2_exact)))
    angle_EAD_rad = math.acos(float(cos_EAD_exact))
    angle_EAD_deg = round(math.degrees(angle_EAD_rad))

    # Chuỗi LaTeX
    c_tex = sp.latex(c)
    b_tex = sp.latex(b)
    a_tex = sp.latex(a)
    BE_tex = sp.latex(BE_exact)
    cos_B_tex = sp.latex(cos_B)
    cos_C_tex = sp.latex(cos_C)
    AE2_tex = sp.latex(AE2_exact)
    AD2_tex = sp.latex(AD2_exact)
    ED_tex = sp.latex(ED_exact)
    ED2_tex = sp.latex(ED2_exact)
    cos_EAD_tex = sp.latex(cos_EAD_exact)

    tan_B = sp.Rational(b, c)
    tan_B_tex = sp.latex(tan_B)

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho tam giác $ABC$ có $AB = %s; AC = %s; \\widehat{BAC} = 90^\\circ$. Gọi $D, E$ là các điểm thuộc cạnh $BC$ sao cho $CD = BE = %s BC$.'''                  
                     %(c_tex, b_tex, k_str))

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Tam giác $ABC$ không phải là tam giác vuông cân'
    nb_da_1_s = 'Tam giác $ABC$ vuông cân'
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Ta có $AB = %s, AC = %s \\Rightarrow AB \\neq AC$. \\\\
                       Do đó tam giác $ABC$ vuông tại $A$ nhưng không cân.'''
                %(c_tex, b_tex))

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
    th_da_1_d = '\\True Độ dài cạnh $BC = %s$' %(a_tex)  
    th_da_1_s = 'Độ dài cạnh $BC = %s$' %(sp.latex(a + 2))   
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Áp dụng định lí Pythagore trong tam giác vuông $ABC$, ta có: \\\\
                       $BC = \\sqrt{AB^2 + AC^2} = \\sqrt{%s^2 + %s^2} = \\sqrt{%s} = %s$.'''       
               %(c_tex, b_tex, sp.latex(c**2 + b**2), a_tex))

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
    vd_da_1_d = '\\True $\\tan \\widehat{ABC} = %s$' %(tan_B_tex)  
    vd_da_1_s = 'Số đo góc $\\widehat{ABC} = 60^\\circ$'  
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Xét tam giác vuông $ABC$, ta có $\\tan \\widehat{ABC} = \\frac{AC}{AB} = \\frac{%s}{%s} = %s$. \\\\
                       (Lưu ý: Góc này không bằng $60^\\circ$).'''  
               %(b_tex, c_tex, tan_B_tex))

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
    vdc_da_1_d = '\\True Số đo góc $\\widehat{EAD} \\approx %s^\\circ$' %(angle_EAD_deg) 
    vdc_da_1_s = 'Số đo góc $\\widehat{EAD} \\approx %s^\\circ$' %(angle_EAD_deg + random.choice([5, 10, 15])) 
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Ta có $BC = %s \\Rightarrow BE = CD = %s \\cdot %s = %s$. \\\\
                        Xét tam giác $ABC$ vuông tại $A$: $\\cos B = \\frac{AB}{BC} = \\frac{%s}{%s} = %s$; $\\cos C = \\frac{AC}{BC} = \\frac{%s}{%s} = %s$. \\\\
                        Áp dụng định lí côsin trong $\\triangle ABE$: \\\\
                        $AE^2 = AB^2 + BE^2 - 2 \\cdot AB \\cdot BE \\cdot \\cos B = %s^2 + \\left(%s\\right)^2 - 2 \\cdot %s \\cdot %s \\cdot %s = %s$. \\\\
                        Áp dụng định lí côsin trong $\\triangle ACD$: \\\\
                        $AD^2 = AC^2 + CD^2 - 2 \\cdot AC \\cdot CD \\cdot \\cos C = %s^2 + \\left(%s\\right)^2 - 2 \\cdot %s \\cdot %s \\cdot %s = %s$. \\\\
                        Vì $E, D$ thuộc đoạn $BC$ và $BE + CD = 2 \\cdot %s = %s < BC$ nên $E$ nằm giữa $B$ và $D$. \\\\
                        Độ dài $ED = BC - BE - CD = %s - %s - %s = %s \\Rightarrow ED^2 = %s$. \\\\
                        Áp dụng hệ quả định lí côsin trong $\\triangle AED$: \\\\
                        $\\cos \\widehat{EAD} = \\frac{AE^2 + AD^2 - ED^2}{2 \\cdot AE \\cdot AD} = \\frac{%s + %s - %s}{2 \\cdot \\sqrt{%s} \\cdot \\sqrt{%s}} = %s$. \\\\
                        Suy ra $\\widehat{EAD} \\approx %s^\\circ$.'''
               %(a_tex, k_str, a_tex, BE_tex,
                 c_tex, a_tex, cos_B_tex, b_tex, a_tex, cos_C_tex,
                 c_tex, BE_tex, c_tex, BE_tex, cos_B_tex, AE2_tex,
                 b_tex, BE_tex, b_tex, BE_tex, cos_C_tex, AD2_tex,
                 BE_tex, sp.latex(2*BE_exact),
                 a_tex, BE_tex, BE_tex, ED_tex, ED2_tex,
                 AE2_tex, AD2_tex, ED2_tex, AE2_tex, AD2_tex, cos_EAD_tex,
                 angle_EAD_deg))

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

