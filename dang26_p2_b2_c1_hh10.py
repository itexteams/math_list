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


def bt_dang26_p2_b2_c1_hh10(self):
    # Khai báo biến và random số liệu
    triples = [(3, 5), (4, 5), (5, 13), (12, 13)]
    u, v = random.choice(triples)
    c = random.randint(3, 8)
    b = random.randint(3, 8)
    while b == c:
        b = random.randint(3, 8)

    cosA = sp.Rational(u, v)
    sinA = sp.sqrt(1 - cosA**2)

    # Tính cạnh BC (a)
    a_sq = b**2 + c**2 - 2*b*c*cosA
    a = sp.sqrt(a_sq)
    a_false = sp.sqrt(b**2 + c**2 + 2*b*c*cosA) # Cố tình sai dấu để tạo đáp án nhiễu

    # Diện tích tam giác và đường cao
    S = sp.Rational(1, 2) * b * c * sinA
    h_a = 2 * S / a
    h_a_false = 4 * S / a 

    # Trung tuyến và bán kính R_GBC
    mb_sq = sp.Rational(2*(a_sq + c**2) - b**2, 4)
    mc_sq = sp.Rational(2*(a_sq + b**2) - c**2, 4)
    mb = sp.sqrt(mb_sq)
    mc = sp.sqrt(mc_sq)

    gb = sp.simplify(mb * sp.Rational(2, 3))
    gc = sp.simplify(mc * sp.Rational(2, 3))
    S_gbc = sp.simplify(S * sp.Rational(1, 3))

    R_GBC = sp.simplify((a * gb * gc) / (4 * S_gbc))
    R_GBC_false = sp.simplify((a * gb * gc) / (S_gbc)) # Thiếu số 4 dưới mẫu

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho tam giác $ABC$ có $G$ là trọng tâm, $AB = %s, AC = %s, \\cos A = %s$.'''               
                     %(c, b, sp.latex(cosA)))

    ######################################################################## Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True $BC = %s$' % sp.latex(a)
    nb_da_1_s = '$BC = %s$' % sp.latex(a_false)
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Áp dụng định lý côsin trong tam giác $ABC$, ta có: \\\\
    $BC^2 = AB^2 + AC^2 - 2AB \\cdot AC \\cdot \\cos A = %s^2 + %s^2 - 2 \\cdot %s \\cdot %s \\cdot %s = %s$. \\\\
    Suy ra $BC = %s$.'''
                    %(c, b, c, b, sp.latex(cosA), sp.latex(a_sq), sp.latex(a)))

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ######################################################################## Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True $\\sin A = %s$' % sp.latex(sinA)  
    th_da_1_s = '$\\sin A = \\pm %s$' % sp.latex(sinA)   
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)


    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Vì $A$ là một góc trong tam giác nên $\\sin A > 0$. \\\\
    Ta có $\\sin^2 A + \\cos^2 A = 1 \\Rightarrow \\sin A = \\sqrt{1 - \\cos^2 A} = \\sqrt{1 - \\left(%s\\right)^2} = %s$.'''       
               %(sp.latex(cosA), sp.latex(sinA)))

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ######################################################################## Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True Đường cao xuất phát từ đỉnh $A$ của tam giác $ABC$ là $%s$' % sp.latex(h_a)  
    vd_da_1_s = 'Đường cao xuất phát từ đỉnh $A$ của tam giác $ABC$ là $%s$' % sp.latex(h_a_false)  
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Diện tích tam giác $ABC$ là $S = \\frac{1}{2} AB \\cdot AC \\cdot \\sin A = \\frac{1}{2} \\cdot %s \\cdot %s \\cdot %s = %s$. \\\\
    Mặt khác $S = \\frac{1}{2} BC \\cdot h_a \\Rightarrow h_a = \\frac{2S}{BC} = \\frac{2 \\cdot %s}{%s} = %s$.'''  
               %(c, b, sp.latex(sinA), sp.latex(S), sp.latex(S), sp.latex(a), sp.latex(h_a)))

    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ######################################################################## Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = '\\True Bán kính đường tròn ngoại tiếp tam giác $GBC$ bằng $%s$' % sp.latex(R_GBC) 
    vdc_da_1_s = 'Bán kính đường tròn ngoại tiếp tam giác $GBC$ bằng $%s$' % sp.latex(R_GBC_false) 
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Gọi $m_b, m_c$ lần lượt là độ dài các đường trung tuyến kẻ từ $B, C$ của tam giác $ABC$. \\\\
    Ta có $m_b^2 = \\frac{2(BC^2 + AB^2) - AC^2}{4} = \\frac{2(%s + %s) - %s}{4} = %s \\Rightarrow m_b = %s$. \\\\
    $m_c^2 = \\frac{2(BC^2 + AC^2) - AB^2}{4} = \\frac{2(%s + %s) - %s}{4} = %s \\Rightarrow m_c = %s$. \\\\
    Vì $G$ là trọng tâm tam giác $ABC$ nên $GB = \\frac{2}{3}m_b = %s, GC = \\frac{2}{3}m_c = %s$. \\\\
    Diện tích tam giác $GBC$ là $S_{GBC} = \\frac{1}{3} S_{ABC} = \\frac{1}{3} \\cdot %s = %s$. \\\\
    Bán kính đường tròn ngoại tiếp tam giác $GBC$ là: \\\\
    $R = \\frac{BC \\cdot GB \\cdot GC}{4 S_{GBC}} = \\frac{%s \\cdot %s \\cdot %s}{4 \\cdot %s} = %s$.'''
               %(sp.latex(a_sq), c**2, b**2, sp.latex(mb_sq), sp.latex(mb),
                 sp.latex(a_sq), b**2, c**2, sp.latex(mc_sq), sp.latex(mc),
                 sp.latex(gb), sp.latex(gc),
                 sp.latex(S), sp.latex(S_gbc),
                 sp.latex(a), sp.latex(gb), sp.latex(gc), sp.latex(S_gbc), sp.latex(R_GBC)))

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
    str(noidungcauhoi)+ '\n'+
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
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

