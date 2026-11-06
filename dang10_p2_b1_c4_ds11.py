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


def bt_dang10_p2_b1_c4_ds11(self):
    # Khai báo biến
    a = randint(2, 4)
    b = randint(2, 5)
    c = a * b
    d = a * a

    # Nội dung câu hỏi
    noidungcauhoi = ('''\\immini{Xét tam giác $ABC$ có $AC = %sAB$ và $BC = %s \\text{ cm}$. Trên cạnh $AC$ lấy điểm $D$ sao cho $AD = \\dfrac{1}{%s}AC$, trên cạnh $AB$ lấy điểm $E$ sao cho $AE = \\dfrac{1}{%s}AB$, trên cạnh $AD$ lấy điểm $F$ sao cho $AF = \\dfrac{1}{%s}AD$ và tiếp tục lấy các điểm $G,H,I,J \\dots$ (vô hạn lần) theo quy luật đó.}
           {\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (A) at (0,3);
            \\coordinate (B) at (-1,0);
            \\coordinate (C) at (2.5,-1);
            \\coordinate (D) at ($(A)!1/4!(C)$);
            \\coordinate (E) at ($(A)!1/4!(B)$);
            \\coordinate (F) at ($(A)!1/4!(D)$);
            \\draw[line width=1pt] (A)--(B)--(C)--(A) (B)--(D)--(E)--(F);
            \\fill (A) circle (1pt) node[above] {$A$};
            \\fill (B) circle (1pt) node[left] {$B$};
            \\fill (C) circle (1pt) node[right] {$C$};
            \\fill (D) circle (1pt) node[right] {$D$};
            \\fill (E) circle (1pt) node[left] {$E$};
            \\fill (F) circle (1pt) node[right] {$F$};
           \\end{tikzpicture} }'''               
                     %(latex(a),latex(c),latex(d),latex(d),latex(d)
                         ))

    ######################################################################## Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True $\\dfrac{AB}{AC} = \\dfrac{AD}{AB}$'
    nb_da_1_s = '$\\dfrac{AB}{AC} = \\dfrac{AB}{AD}$'
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Ta có $AC=%s AB \\Rightarrow \\dfrac{AB}{AC}=\\dfrac{1}{%s}$.\\\\
    Lại có $AD=\\dfrac{1}{%s} AC=\\dfrac{1}{%s} \\cdot %s AB=\\dfrac{1}{%s} AB \\Rightarrow \\dfrac{AD}{AB}=\\dfrac{1}{%s}$.\\\\
    Vậy $\\dfrac{AB}{AC}=\\dfrac{AD}{AB}$.'''
                %(latex(a),latex(a),latex(d),latex(d),latex(a),latex(a),latex(a))
                )

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
    th_da_1_d = '\\True Tam giác $ABD$ đồng dạng với tam giác $ABC$'
    th_da_1_s = 'Tam giác $ABD$ không đồng dạng với tam giác $ABC$' 
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)


    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Xét tam giác $ABD$ và tam giác $ABC$ có:\\\\
    Góc $\\widehat{A}$ chung.\\\\
    $\\dfrac{AB}{AC}=\\dfrac{AD}{AB}$ (chứng minh trên).\\\\
    Suy ra $\\triangle ABD \\backsim \\triangle ABC$ (c.g.c).'''       
               )

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
    e = Rational(c, a)
    f = Rational(c, d)
    vd_da_1_d = '\\True $BD = %s \\text{ cm}; DE = %s \\text{ cm}$' %(latex(e),latex(f))  
    vd_da_1_s = '$BD = %s \\text{ cm}; DE = %s \\text{ cm}$' %(latex(f),latex(e))  
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Vì $\\triangle ABD \\backsim \\triangle ABC$ (cmt) $\\Rightarrow \\dfrac{BD}{BC}=\\dfrac{AB}{AC}=\\dfrac{1}{%s} \\Rightarrow BD=\\dfrac{1}{%s} BC=\\dfrac{1}{%s} \\cdot %s=%s \\text{ (cm)}$.\\\\
    Theo đề bài ta có $\\dfrac{AE}{AB}=\\dfrac{1}{%s} \\Rightarrow \\dfrac{AE}{AD}=\\dfrac{\\dfrac{1}{%s} AB}{\\dfrac{1}{%s} AB}=\\dfrac{1}{%s}$.\\\\
    Xét tam giác $ADE$ và tam giác $ABD$ có:\\\\
    Góc $\\widehat{A}$ chung.\\\\
    $\\dfrac{AE}{AD}=\\dfrac{AD}{AB}=\\dfrac{1}{%s}$.\\\\
    Suy ra $\\triangle ADE \\backsim \\triangle ABD$ (c.g.c).\\\\
    Suy ra $\\dfrac{DE}{BD}=\\dfrac{AE}{AD}=\\dfrac{1}{%s} \\Rightarrow DE=\\dfrac{1}{%s} BD=\\dfrac{1}{%s} \\cdot %s=%s \\text{ (cm)}$.'''  
               %(latex(a),latex(a),latex(a),latex(c),latex(e),latex(d),latex(d),latex(a),latex(a),latex(a),latex(a),latex(a),latex(a),latex(e),latex(f)
                    ))

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
    g = Rational(c*a, a-1)
    vdc_da_1_d = '\\True Độ dài đường gấp khúc $CBDEFGH\\dots$ bằng $%s \\text{ cm}$' %(latex(g)) 
    vdc_da_1_s = 'Độ dài đường gấp khúc $CBDEFGH\\dots$ bằng $%s \\text{ cm}$' %(latex(c)) 
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Lập luận tương tự, ta có dãy độ dài các đoạn thẳng $BC, BD, DE, EF, FG, \\dots$ lập thành một cấp số nhân lùi vô hạn với công bội $q=\\dfrac{1}{%s}$ và số hạng đầu $u_1=BC=%s$.\\\\
    Độ dài đường gấp khúc $CBDEFGH\\dots$ bằng tổng của cấp số nhân lùi vô hạn này.\\\\
    $S = \\dfrac{u_1}{1-q} = \\dfrac{%s}{1-\\dfrac{1}{%s}} = %s \\text{ (cm)}$.'''
               %(latex(a),latex(c),latex(c),latex(a),latex(g)
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
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

