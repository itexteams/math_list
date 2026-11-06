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


def bt_dang15_p2_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo các thông số cơ bản
            a_side = symbols('a')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình lăng trụ $ABC.A'B'C'$ có $ABC$ là tam giác đều và $ABB'A'$ là hình vuông. Gọi $M$ là trung điểm của $BC$.''')

            ########################################################################
            # Nhận biết: Góc giữa AB và B'C'
            ########################################################################
            nb_da_1_d = '\\True Số đo góc giữa hai đường thẳng $AB$ và $B\'C\'$ bằng $60^\\circ$'
            nb_da_1_s = 'Số đo góc giữa hai đường thẳng $AB$ và $B\'C\'$ bằng $30^\\circ$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Vì $B'C' \\parallel BC$ nên $(AB, B'C') = (AB, BC) = \\widehat{ABC}$. \\\\
            Vì $\\triangle ABC$ đều nên $\\widehat{ABC} = 60^\\circ$. Vậy $(AB, B'C') = 60^\\circ$.''')

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip([nb_da_1], list_nb_2))
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu: Góc giữa AB và CC'
            ########################################################################
            th_da_1_d = 'Số đo góc giữa hai đường thẳng $AB$ và $CC\'$ bằng $45^\\circ$' 
            th_da_1_s = '\\True Số đo góc giữa hai đường thẳng $AB$ và $CC\'$ bằng $90^\\circ$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Ta có $CC' \\parallel BB'$. Do đó $(AB, CC') = (AB, BB')$. \\\\
            Vì $ABB'A'$ là hình vuông nên $AB \\perp BB'$, hay $(AB, BB') = 90^\\circ$.''')

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip([th_da_1], list_th_2))
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng: Góc giữa AM và A'C'
            ########################################################################
            vd_da_1_d = '\\True Số đo góc giữa hai đường thẳng $AM$ và $A\'C\'$ bằng $30^\\circ$'
            vd_da_1_s = 'Số đo góc giữa hai đường thẳng $AM$ và $A\'C\'$ bằng $60^\\circ$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Ta có $A'C' \\parallel AC$ nên $(AM, A'C') = (AM, AC) = \\widehat{MAC}$. \\\\
            Trong tam giác đều $ABC$, trung tuyến $AM$ đồng thời là đường phân giác, nên $\\widehat{MAC} = \\frac{1}{2} \\widehat{BAC} = 30^\\circ$.''')

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip([vd_da_1], list_vd_2))
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao: Góc giữa A'M và BB'
            ########################################################################
            vdc_da_1_d = 'Số đo góc giữa hai đường thẳng $A\'M$ và $BB\'$ bằng $60^\\circ$' 
            vdc_da_1_s = '\\True Số đo góc giữa hai đường thẳng $A\'M$ và $BB\'$ không bằng $60^\\circ$' 
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Vì $BB' \\parallel AA'$ nên $(A'M, BB') = (A'M, AA') = \\widehat{MA'A}$. \\\\
            Đặt $AB = a$. Vì $ABB'A'$ là hình vuông nên $AA' = a$ và $AA' \\perp (ABC)$. \\\\
            Trong tam giác đều $ABC$, $AM = \\frac{a\\sqrt{3}}{2}$. \\\\
            Xét tam giác $A'AM$ vuông tại $A$: $\\tan \\widehat{MA'A} = \\frac{AM}{AA'} = \\frac{a\\sqrt{3}/2}{a} = \\frac{\\sqrt{3}}{2} \\neq \\tan 60^\\circ$.''')

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Vẽ hình TikZ - Đã sửa nhãn thành A', B', C'
            tikz_hinh_ve = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round]
            \\coordinate (A) at (0,0);
            \\coordinate (B) at (1.2,-1.2);
            \\coordinate (C) at (3.5,0);
            \\coordinate (M) at ($(B)!0.5!(C)$);
            \\coordinate (A1) at (0,3.5);
            \\coordinate (B1) at ($(B)+(A1)-(A)$);
            \\coordinate (C1) at ($(C)+(A1)-(A)$);
            \\draw (A)--(A1) (A)--(B) (A1)--(B1)--(C1)--cycle (B)--(B1) (C)--(C1) (B)--(C);
            \\draw[dashed]   (A)--(C) (A1)--(M) (A)--(M);
            \\foreach \\p/\\pos/\\label in {A/left/A, B/below/B, C/right/C, A1/above/A', B1/below/B', C1/right/C', M/below/M}
            { \\fill (\\p) ;
              \\node[\\pos] at (\\p) {$\\label$};}
            \\end{tikzpicture}
            \\end{center}''')

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # Xuất nội dung (Không sử dụng r-string)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n' +
                tikz_hinh_ve + '\n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

