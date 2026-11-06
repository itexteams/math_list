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


def bt_dang22_p2_b1_c1_hh11(self):
    # Khai báo biến - Cố định tên các điểm trong hình học theo đúng ảnh gốc
    A, B, C, D, I, J, M, N, E, F = 'A', 'B', 'C', 'D', 'I', 'J', 'M', 'N', 'E', 'F'

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho tứ diện $%s%s%s%s$. Gọi $%s,%s$ lần lượt là trung điểm của $%s%s,%s%s$, $%s$ là một điểm trên cạnh $%s%s$, $%s$ là một điểm trên cạnh $%s%s$.''' 
                     %(A,B,C,D, I,J, A,D,B,C, M, A,B, N, A,C))

    ######################################################################## Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True $%s%s$ là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$' %(I,J, I,B,C, J,A,D)
    nb_da_1_s = '$%s%s$ là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$' %(A,B, I,B,C, J,A,D)
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''$%s%s$ là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$.\\\\
    Ta có: $%s \\in %s%s, %s%s \\subset (%s%s%s) \\Rightarrow %s \\in (%s%s%s) \\Rightarrow %s%s \\subset (%s%s%s)$.\\\\
    $%s \\in %s%s, %s%s \\subset (%s%s%s) \\Rightarrow %s \\in (%s%s%s) \\Rightarrow %s%s \\subset (%s%s%s)$.\\\\
    Vậy $(%s%s%s) \\cap (%s%s%s) = %s%s$.'''
                    %(I,J, I,B,C, J,A,D,
                      I, A,D, A,D, J,A,D, I, J,A,D, I,J, J,A,D,
                      J, B,C, B,C, I,B,C, J, I,B,C, I,J, I,B,C,
                      I,B,C, J,A,D, I,J))

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
    th_da_1_d = '\\True $%s%s$ là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$' %(N,D, M,N,D, A,D,C)
    th_da_1_s = '$%s%s$ là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$' %(M,D, M,N,D, A,D,C)
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''$%s%s$ là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$.\\\\
    Ta có: $%s \\in (%s%s%s) \\cap (%s%s%s)$ và $%s \\in (%s%s%s) \\cap (%s%s%s)$.\\\\
    Vậy $(%s%s%s) \\cap (%s%s%s) = %s%s$.'''
                    %(N,D, M,N,D, A,D,C,
                      N, M,N,D, A,D,C, D, M,N,D, A,D,C,
                      M,N,D, A,D,C, N,D))

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
    vd_da_1_d = '\\True $%s%s$ là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$' %(B,I, B,C,I, A,B,D)
    vd_da_1_s = '$%s%s$ là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$' %(C,I, B,C,I, A,B,D)
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''$%s%s$ là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$.\\\\
    Ta có $%s \\in (%s%s%s) \\cap (%s%s%s)$ và $%s \\in %s%s \\subset (%s%s%s) \\Rightarrow %s \\in (%s%s%s) \\cap (%s%s%s)$.\\\\
    Vậy $(%s%s%s) \\cap (%s%s%s) = %s%s$.'''
                    %(B,I, B,C,I, A,B,D,
                      B, B,C,I, A,B,D, I, A,D, A,B,D, I, B,C,I, A,B,D,
                      B,C,I, A,B,D, B,I))

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
    vdc_da_1_d = '\\True Giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$ là đường thẳng đi qua giao điểm của $%s%s$ và $%s%s$' %(I,B,C, D,M,N, D,N, C,I)
    vdc_da_1_s = 'Giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$ song song với đường thẳng $%s%s$' %(I,B,C, D,M,N, I,J)
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    tikz_str = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (v1) at (2.5,4.5);
    \\coordinate (v2) at (0,0);
    \\coordinate (v3) at (3.5,-1.5);
    \\coordinate (v4) at (7,0);
    \\coordinate (p1) at ($(v1)!0.45!(v4)$);
    \\coordinate (p2) at ($(v2)!0.5!(v3)$);
    \\coordinate (p3) at ($(v1)!0.4!(v2)$);
    \\coordinate (p4) at ($(v1)!0.6!(v3)$);
    \\coordinate (e_node) at (intersection of v4--p4 and v3--p1);
    \\coordinate (f_node) at (intersection of v4--p3 and v2--p1);
    \\draw[line width=1pt] (v1)--(v2)--(v3)--(v4)--(v1) (v1)--(v3) (p3)--(p4) (p4)--(v4) (p1)--(v3);
    \\draw[line width=1pt, dashed] (v2)--(v4) (p3)--(v4) (p1)--(v2) (p1)--(p2) (e_node)--(f_node);
    \\fill (v1) circle (1pt) node[above] {$%s$};
    \\fill (v2) circle (1pt) node[left] {$%s$};
    \\fill (v3) circle (1pt) node[below] {$%s$};
    \\fill (v4) circle (1pt) node[right] {$%s$};
    \\fill (p1) circle (1pt) node[right] {$%s$};
    \\fill (p2) circle (1pt) node[below left] {$%s$};
    \\fill (p3) circle (1pt) node[left] {$%s$};
    \\fill (p4) circle (1pt) node[right] {$%s$};
    \\fill (e_node) circle (1pt) node[below] {$%s$};
    \\fill (f_node) circle (1pt) node[above] {$%s$};
    \\end{tikzpicture}
    \\end{center}''' %(A, B, C, D, I, J, M, N, E, F))

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Gọi $%s = %s%s \\cap %s%s$ (trong mặt phẳng $(%s%s%s)$) và $%s = %s%s \\cap %s%s$ (trong mặt phẳng $(%s%s%s)$).\\\\
    Ta có: $\\begin{cases} %s \\in %s%s, %s%s \\subset (%s%s%s) \\\\ %s \\in %s%s, %s%s \\subset (%s%s%s) \\end{cases} \\Rightarrow %s \\in (%s%s%s) \\cap (%s%s%s) \\quad (1)$.\\\\
    Tương tự: $\\begin{cases} %s \\in %s%s, %s%s \\subset (%s%s%s) \\\\ %s \\in %s%s, %s%s \\subset (%s%s%s) \\end{cases} \\Rightarrow %s \\in (%s%s%s) \\cap (%s%s%s) \\quad (2)$.\\\\
    Từ (1) và (2) suy ra $(%s%s%s) \\cap (%s%s%s) = %s%s$. \\\\
    Do đó giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$ là đường thẳng $%s%s$ (không song song với đường thẳng $%s%s$).''' 
                    %(E, D,N, C,I, A,C,D, F, D,M, B,I, A,B,D,
                      E, D,N, D,N, D,M,N, E, I,C, I,C, I,B,C, E, D,M,N, I,B,C,
                      F, D,M, D,M, D,M,N, F, B,I, B,I, I,B,C, F, D,M,N, I,B,C,
                      D,M,N, I,B,C, E,F,
                      I,B,C, D,M,N, E,F, I,J))

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
        '\\loigiai{ \n'+tikz_str+
        '\n\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n\\end{minipage}\n\n')
    return content

