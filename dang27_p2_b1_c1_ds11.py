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


def bt_dang27_p2_b1_c1_ds11(self):
            # Khai báo biến
            # B3-Suy nghĩ tìm cách random bài toán
            # Để sinh ra nhiều bài toán khác nhau, ta chọn ngẫu nhiên thứ tự quay các đỉnh hình vuông: (A, B, C, D), (B, C, D, a) hoặc (C, D, A, B).
            label_variants = [
                ("A", "B", "C", "D"),
                ("B", "C", "D", "A"),
                ("C", "D", "A", "B"),
                ("D", "A", "B", "C")
            ]
            v1, v2, v3, v4 = random.choice(label_variants)

            # Vẽ hình vuông ABCD tâm O bằng TikZ đảm bảo độ dày nét đúng 1pt
            tikz_image = ('''\\begin{center} \\begin{tikzpicture}[scale=1.5, line width=1pt]
            \\coordinate (C) at (0,0);
            \\coordinate (D) at (2,0);
            \\coordinate (A) at (2,2);
            \\coordinate (B) at (0,2);
            \\coordinate (O) at (1,1);
            \\draw (A) -- (B) -- (C) -- (D) -- cycle;
            \\draw (A) -- (C);
            \\draw (B) -- (D);
            \\filldraw[fill=blue!20] (A) circle (0pt) node[above right] {$%s$};
            \\filldraw[fill=blue!20] (B) circle (0pt) node[above left] {$%s$};
            \\filldraw[fill=blue!20] (C) circle (0pt) node[below left] {$%s$};
            \\filldraw[fill=blue!20] (D) circle (0pt) node[below right] {$%s$};
            \\filldraw[fill=blue!20] (O) circle (0pt) node[below] {$O$};
            \\end{tikzpicture} \\end{center} ''' %(v1, v2, v3, v4))

            # Nội dung câu hỏi sử dụng định dạng %s
            noidungcauhoi = ('''Cho hình vuông $%s%s%s%s$ tâm $O$ (tham khảo hình vẽ). %s Xét tính đúng sai của các khẳng định sau:''' %(v1, v2, v3, v4, tikz_image))

            ########################################################################
            # Nhận biết ############################################
            # Khẳng định a
            nb_da_1_s = 'sđ$(%s%s; %s%s) = 90^\\circ$' %(v1, v4, v1, v2)
            nb_da_1_d = '\\True sđ$(%s%s; %s%s) = -90^\\circ + k360^\\circ, k \\in \\mathbb{Z}$' %(v1, v4, v1, v2)
            list_nb_da_1 = [nb_da_1_s, nb_da_1_d]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Góc lượng giác $(%s%s; %s%s)$ quay từ tia $%s%s$ sang tia $%s%s$ theo chiều âm (chiều kim đồng hồ) một góc $90^\\circ$, do đó số đo của góc lượng giác phải là $-90^\\circ + k360^\\circ, k \\in \\mathbb{Z}$.''' %(v1, v4, v1, v2, v1, v4, v1, v2))
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Khẳng định b
            th_da_1_d = '\\True sđ$(%s%s; %s%s) = 180^\\circ + k360^\\circ, k \\in \\mathbb{Z}$' %(v1, v2, v4, v3)
            th_da_1_s = 'sđ$(%s%s; %s%s) = 0^\\circ + k360^\\circ, k \\in \\mathbb{Z}$' %(v1, v2, v4, v3)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Hai vectơ $\\vec{%s%s}$ và $\\vec{%s%s}$ là hai vectơ đối nhau (ngược hướng), do đó góc giữa chúng bằng $180^\\circ$. Vậy họ số đo góc lượng giác tương ứng là $180^\\circ + k360^\\circ, k \\in \\mathbb{Z}$.''' %(v1, v2, v3, v4))
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Khẳng định c
            vd_da_1_s = 'sđ$(%s%s; %s%s) = -45^\\circ + k360^\\circ, k \\in \\mathbb{Z}$' %(v1, v2, v1, v3)
            vd_da_1_d = '\\True sđ$(%s%s; %s%s) = 45^\\circ + k360^\\circ, k \\in \\mathbb{Z}$' %(v1, v2, v1, v3)
            list_vd_da_1 = [vd_da_1_s, vd_da_1_d]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Tia $%s%s$ là tia phân giác của góc $\\widehat{%s%s%s}$. Quay từ tia $%s%s$ sang tia $%s%s$ tuân theo chiều dương (ngược chiều kim đồng hồ) một góc đúng bằng $45^\\circ$, do đó số đo tổng quát là $45^\\circ + k360^\\circ, k \\in \\mathbb{Z}$.''' %(v1, v3, v2, v1, v4, v1, v2, v1, v3))
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Khẳng định d
            vdc_da_1_d = '\\True sđ$(O%s; O%s) = -270^\\circ + k360^\\circ, k \\in \\mathbb{Z}$' %(v1, v2)
            vdc_da_1_s = 'sđ$(O%s; O%s) = 270^\\circ + k360^\\circ, k \\in \\mathbb{Z}$' %(v1, v2)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Quay từ tia $O%s$ sang tia $O%s$ theo chiều dương một góc vuông $90^\\circ$, nên số đo góc lượng giác là $90^\\circ + k360^\\circ, k \\in \\mathbb{Z}$.\\\\
            Khi chọn $k = -1$, ta có $90^\\circ - 360^\\circ = -270^\\circ$. Do đó, họ góc lượng giác này viết dưới dạng $-270^\\circ + k360^\\circ, k \\in \\mathbb{Z}$ là chính xác.''' %(v1, v2))
            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng để bảo toàn logic trắc nghiệm Đúng/Sai
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list sau khi chọn lọc ngẫu nhiên hợp lệ
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

            # Xuất cấu trúc câu hỏi hoàn chỉnh với định dạng chuỗi %s
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

