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


def bt_dang11_p2_b1_c1_hh12(self):
            # Khai báo biến
            # Khai báo biến và tạo ngẫu nhiên tham số n
            n = random.randint(2, 5)
            sum_coeff = 2 * (n + 1)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$. Gọi $O$ là giao điểm của $AC$ và $BD$.''')

            # Code TikZ cho phần lời giải
            tikz_code = '''\\begin{center}
            \\begin{tikzpicture}[scale=0.9, line join=round, line width=1pt, line cap=round]
                \\coordinate (A) at (1.5,1.5);
                \\coordinate (B) at (0,0);
                \\coordinate (C) at (5,0);
                \\coordinate (D) at (3.5,1.5);
                \\coordinate (S) at (2.5,4);
                \\coordinate (O) at (intersection of A--C and B--D);
                \\draw[dashed] (B) -- (A) -- (D) (A) -- (C) (B) -- (D) (S) -- (A) (S) -- (O) (S) -- (D) (D) -- (C);
                \\draw (S) -- (B) -- (C) -- (S);
                \\fill (S) circle (0.5pt) node[above] {$S$};
                \\fill (A) circle (0.5pt) node[left] {$A$};
                \\fill (B) circle (0.5pt) node[left] {$B$};
                \\fill (C) circle (0.5pt) node[right] {$C$};
                \\fill (D) circle (0.5pt) node[right] {$D$};
                \\fill (O) circle (0.5pt) node[below] {$O$};
            \\end{tikzpicture}
            \\end{center}'''

            ######################################################################## Nhận biết ############################################

            # Các đáp án
            nb_da_1_d = '\\True Nếu $\\overrightarrow{SA} + \\overrightarrow{SB} + %s\\overrightarrow{SC} + %s\\overrightarrow{SD} = %s\\overrightarrow{SO}$ thì $ABCD$ là hình thang' % (n, n, sum_coeff)
            nb_da_1_s = 'Nếu $\\overrightarrow{SA} + \\overrightarrow{SB} + %s\\overrightarrow{SC} + %s\\overrightarrow{SD} = %s\\overrightarrow{SO}$ thì $ABCD$ là hình chữ nhật' % (n, n, sum_coeff)
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Đúng vì $\\overrightarrow{SA} + \\overrightarrow{SB} + %s\\overrightarrow{SC} + %s\\overrightarrow{SD} = %s\\overrightarrow{SO} \\Leftrightarrow \\overrightarrow{OA} + \\overrightarrow{OB} + %s\\overrightarrow{OC} + %s\\overrightarrow{OD} = \\vec{0}$. \\\\
            Vì $O, A, C$ và $O, B, D$ thẳng hàng nên đặt $\\overrightarrow{OA} = k\\overrightarrow{OC}; \\overrightarrow{OB} = m\\overrightarrow{OD}$ \\\\
            $\\Rightarrow (k+%s)\\overrightarrow{OC} + (m+%s)\\overrightarrow{OD} = \\vec{0}$. \\\\
            Mà $\\overrightarrow{OC}, \\overrightarrow{OD}$ không cùng phương nên $k = -%s$ và $m = -%s \\Rightarrow \\frac{OA}{OC} = \\frac{OB}{OD} = %s \\Rightarrow AB \\parallel CD$. Vậy $ABCD$ là hình thang.''' % (n, n, sum_coeff, n, n, n, n, n, n, n))
            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Nếu $ABCD$ là hình bình hành thì $\\overrightarrow{SA} + \\overrightarrow{SB} + \\overrightarrow{SC} + \\overrightarrow{SD} = 4\\overrightarrow{SO}$'
            th_da_1_s = 'Nếu $ABCD$ là hình bình hành thì $\\overrightarrow{SA} + \\overrightarrow{SB} + \\overrightarrow{SC} + \\overrightarrow{SD} = 2\\overrightarrow{SO}$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Đúng. Biến đổi bằng cách chêm điểm $O$ vào vế trái: \\\\
            $\\overrightarrow{SA} + \\overrightarrow{SB} + \\overrightarrow{SC} + \\overrightarrow{SD} = 4\\overrightarrow{SO} + \\left(\\overrightarrow{OA} + \\overrightarrow{OC}\\right) + \\left(\\overrightarrow{OB} + \\overrightarrow{OD}\\right) = 4\\overrightarrow{SO} + \\vec{0} + \\vec{0} = 4\\overrightarrow{SO}$ (do $O$ là tâm hình bình hành).''')

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Có trường hợp $ABCD$ là hình thang nhưng $\\overrightarrow{SA} + \\overrightarrow{SB} + %s\\overrightarrow{SC} + %s\\overrightarrow{SD} \\ne %s\\overrightarrow{SO}$' % (n, n, sum_coeff)
            vd_da_1_s = 'Nếu $ABCD$ là hình thang thì $\\overrightarrow{SA} + \\overrightarrow{SB} + %s\\overrightarrow{SC} + %s\\overrightarrow{SD} = %s\\overrightarrow{SO}$' % (n, n, sum_coeff)
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Đúng. Vì nếu $ABCD$ là hình thang có 2 đáy là $AD, BC$ thì đẳng thức $\\overrightarrow{SA} + \\overrightarrow{SB} + %s\\overrightarrow{SC} + %s\\overrightarrow{SD} = %s\\overrightarrow{SO}$ sẽ sai (đẳng thức chỉ xảy ra khi $AB \\parallel CD$ và $AB = %s CD$).''' % (n, n, sum_coeff, n))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Nếu $\\overrightarrow{SA} + \\overrightarrow{SB} + \\overrightarrow{SC} + \\overrightarrow{SD} = 4\\overrightarrow{SO}$ thì $ABCD$ là hình bình hành'
            vdc_da_1_s = 'Nếu $\\overrightarrow{SA} + \\overrightarrow{SB} + \\overrightarrow{SC} + \\overrightarrow{SD} = 4\\overrightarrow{SO}$ thì $ABCD$ là hình thang cân'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Đúng. Tương tự như phân tích ở đáp án A với hệ số bằng $1$. Ta có $k = -1, m = -1 \\Rightarrow O$ là trung điểm 2 đường chéo. Vậy $ABCD$ là hình bình hành.''')

            # Đưa các lời giải vào danh sách lời giải
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
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
               '{'+str(shuffled_answers_nb[0])+'}\n'
               '{'+str(shuffled_answers_th[0])+'}\n'
               '{'+str(shuffled_answers_vd[0])+'}\n'
               '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n' + tikz_code + '\n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

