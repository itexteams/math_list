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


def bt_dang29_p2_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Các tham số ký hiệu trong bài
            sym_a, sym_b, sym_c, sym_d = 'a', 'b', 'c', 'd'

            # Nội dung câu hỏi có kèm hình TikZ mô phỏng chính xác đường cong trong mẫu
            noidungcauhoi = ('''Cho hàm số $y = f(x) = \\frac{%sx^2+%sx+%s}{x+%s}$ có đồ thị như hình vẽ.
            \\begin{center}
            \\begin{tikzpicture}[scale=0.8, >=stealth, font=\\footnotesize]
            \\draw[->] (-5,0) -- (2,0) node[above] {$x$};
            \\draw[->] (0,-5) -- (0,4) node[right] {$y$};
            \\node[below right] at (0,0) {$O$};
            \\draw[dashed, thick] (-1,-5) -- (-1,4);
            \\draw[dashed, thick] (-5,3) -- (1,-3);
            \\clip (-5,-5) rectangle (1,4);
            \\draw[thick, red, smooth, samples=100, domain=-5:-1.2] plot (\\x, {-\\x - 2 + 1/(\\x+1)});
            \\draw[thick, red, smooth, samples=100, domain=-0.8:1] plot (\\x, {-\\x - 2 + 1/(\\x+1)});
            \\end{tikzpicture}
            \\end{center}''' % (sym_a, sym_b, sym_c, sym_d))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $%s < 0$' % sym_a
            nb_da_1_s = '$%s > 0$' % sym_a

            loigiai_nb_d = ('''Từ đồ thị ta thấy đường tiệm cận xiên đi xuống từ trái sang phải nên hệ số góc $%s < 0$. \\\\ 
            Mệnh đề đúng.''' % sym_a)

            loigiai_nb_s = ('''Từ đồ thị ta thấy đường tiệm cận xiên đi xuống từ trái sang phải nên hệ số góc $%s < 0$. \\\\ 
            Mệnh đề sai.''' % sym_a)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $%s > 0$' % sym_d
            th_da_1_s = '$%s < 0$' % sym_d

            loigiai_th_d = ('''Từ đồ thị ta thấy đường tiệm cận đứng $x = -%s$ nằm bên trái trục tung nên $-%s < 0 \\Rightarrow %s > 0$. \\\\ 
            Mệnh đề đúng.''' % (sym_d, sym_d, sym_d))

            loigiai_th_s = ('''Từ đồ thị ta thấy đường tiệm cận đứng $x = -%s$ nằm bên trái trục tung nên $-%s < 0 \\Rightarrow %s > 0$. \\\\ 
            Mệnh đề sai.''' % (sym_d, sym_d, sym_d))

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $%s < 0$' % sym_c
            vd_da_1_s = '$%s > 0$' % sym_c

            loigiai_vd_d = ('''Giao điểm của đồ thị với trục tung là điểm có tọa độ $\\left(0; \\frac{%s}{%s}\\right)$. \\\\ 
            Từ đồ thị ta thấy giao điểm này nằm dưới trục hoành nên $\\frac{%s}{%s} < 0$. \\\\ 
            Mà $%s > 0$ (chứng minh trên) nên $%s < 0$. \\\\ 
            Mệnh đề đúng.''' % (sym_c, sym_d, sym_c, sym_d, sym_d, sym_c))

            loigiai_vd_s = ('''Giao điểm của đồ thị với trục tung là điểm có tọa độ $\\left(0; \\frac{%s}{%s}\\right)$. \\\\ 
            Từ đồ thị ta thấy giao điểm này nằm dưới trục hoành nên $\\frac{%s}{%s} < 0$. \\\\ 
            Mà $%s > 0$ (chứng minh trên) nên $%s < 0$. \\\\ 
            Mệnh đề sai.''' % (sym_c, sym_d, sym_c, sym_d, sym_d, sym_c))

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True $%s < 2%s%s$' % (sym_b, sym_a, sym_d)
            vdc_da_1_s = '$%s > 2%s%s$' % (sym_b, sym_a, sym_d)

            loigiai_vdc_d = ('''Ta có $y = \\frac{%sx^2+%sx+%s}{x+%s} = %sx + %s - %s%s + \\frac{%s-%s(%s-%s%s)}{x+%s}$. \\\\
            Đường tiệm cận xiên có phương trình $y = %sx + %s - %s%s$. \\\\
            Giao điểm của hai đường tiệm cận là $I(-%s; -%s%s + %s - %s%s) = I(-%s; %s - 2%s%s)$. \\\\
            Từ đồ thị ta thấy giao điểm $I$ nằm ở góc phần tư thứ ba, do đó tung độ $y_I < 0 \\Leftrightarrow %s - 2%s%s < 0 \\Leftrightarrow %s < 2%s%s$. \\\\ 
            Mệnh đề đúng.''' % (sym_a, sym_b, sym_c, sym_d, sym_a, sym_b, sym_a, sym_d, sym_c, sym_d, sym_b, sym_a, sym_d, sym_d, sym_a, sym_b, sym_a, sym_d, sym_d, sym_a, sym_d, sym_b, sym_a, sym_d, sym_d, sym_b, sym_a, sym_d, sym_b, sym_a, sym_d, sym_b, sym_a, sym_d))

            loigiai_vdc_s = ('''Ta có $y = \\frac{%sx^2+%sx+%s}{x+%s} = %sx + %s - %s%s + \\frac{%s-%s(%s-%s%s)}{x+%s}$. \\\\
            Đường tiệm cận xiên có phương trình $y = %sx + %s - %s%s$. \\\\
            Giao điểm của hai đường tiệm cận là $I(-%s; -%s%s + %s - %s%s) = I(-%s; %s - 2%s%s)$. \\\\
            Từ đồ thị ta thấy giao điểm $I$ nằm ở góc phần tư thứ ba, do đó tung độ $y_I < 0 \\Leftrightarrow %s - 2%s%s < 0 \\Leftrightarrow %s < 2%s%s$. \\\\ 
            Mệnh đề sai.''' % (sym_a, sym_b, sym_c, sym_d, sym_a, sym_b, sym_a, sym_d, sym_c, sym_d, sym_b, sym_a, sym_d, sym_d, sym_a, sym_b, sym_a, sym_d, sym_d, sym_a, sym_d, sym_b, sym_a, sym_d, sym_d, sym_b, sym_a, sym_d, sym_b, sym_a, sym_d, sym_b, sym_a, sym_d))


            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Gom nhóm phương án và lời giải để đồng bộ logic khi xáo trộn
            list_nb = [(nb_da_1_d, loigiai_nb_d), (nb_da_1_s, loigiai_nb_s)]
            list_th = [(th_da_1_d, loigiai_th_d), (th_da_1_s, loigiai_th_s)]
            list_vd = [(vd_da_1_d, loigiai_vd_d), (vd_da_1_s, loigiai_vd_s)]
            list_vdc = [(vdc_da_1_d, loigiai_vdc_d), (vdc_da_1_s, loigiai_vdc_s)]

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb = random.choice(list_nb)
                th = random.choice(list_th)
                vd = random.choice(list_vd)
                vdc = random.choice(list_vdc)

                answers = [nb[0], th[0], vd[0], vdc[0]]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list (Đảm bảo câu hỏi đi kèm đúng với lời giải tương ứng)
            list_nb_1 = [nb[0]]
            list_nb_2 = [nb[1]]

            list_th_1 = [th[0]]
            list_th_2 = [th[1]]

            list_vd_1 = [vd[0]]
            list_vd_2 = [vd[1]]

            list_vdc_1 = [vdc[0]]
            list_vdc_2 = [vdc[1]]

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

