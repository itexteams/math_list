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


def bt_dang14_p2_b1_c1_hh12(self):
            # Khai báo biến
            # Khai báo biến và tạo ngẫu nhiên độ dài cạnh hình lập phương
            k = random.randint(1, 4)
            edge = "a" if k == 1 else f"{k}a"
            edge_sq = "a^2" if k == 1 else f"{k**2}a^2"
            frac_false = "\\frac{a^2}{2}" if k == 1 else f"\\frac{{{k**2}a^2}}{{2}}"
            neg_frac_false = "-\\frac{a^2}{2}" if k == 1 else f"-\\frac{{{k**2}a^2}}{{2}}"
            c_true = "a\\sqrt{3}" if k == 1 else f"{k}a\\sqrt{{3}}"
            c_false = "a\\sqrt{2}" if k == 1 else f"{k}a\\sqrt{{2}}"
            d_true = "4a" if k == 1 else f"{4*k}a"
            d_false = "2a" if k == 1 else f"{2*k}a"

            # Nội dung câu hỏi và hình vẽ TikZ
            noidungcauhoi = ('''Cho hình lập phương $ABCD.A'B'C'D'$ có cạnh bằng $%s$. Gọi $O, O'$ lần lượt là tâm của hình vuông $ABCD$ và $A'B'C'D'$.
            \\begin{center}
            \\begin{tikzpicture}[scale=0.7, line join=round, line width=1pt, line cap=round]
                \\coordinate (A) at (1.5,1.5);
                \\coordinate (B) at (5.5,1.5);
                \\coordinate (C) at (4,0);
                \\coordinate (D) at (0,0);
                \\coordinate (A') at (1.5,5);
                \\coordinate (B') at (5.5,5);
                \\coordinate (C') at (4,3.5);
                \\coordinate (D') at (0,3.5);
                \\coordinate (O) at (2.75,0.75);
                \\coordinate (O') at (2.75,4.25);
                \\draw[dashed] (D) -- (A) -- (B) (A) -- (A') (A) -- (C) (B) -- (D) ;
                \\draw (D) -- (C) -- (B) -- (B') -- (C') -- (D') -- cycle;
                \\draw (C) -- (C') (D') -- (A') -- (B')--(A') -- (C')--(B') -- (D') ;
                \\fill (A) circle (1.5pt) node[above left] {$A$};
                \\fill (B) circle (1.5pt) node[right] {$B$};
                \\fill (C) circle (1.5pt) node[below right] {$C$};
                \\fill (D) circle (1.5pt) node[below left] {$D$};
                \\fill (A') circle (1.5pt) node[above left] {$A'$};
                \\fill (B') circle (1.5pt) node[above right] {$B'$};
                \\fill (C') circle (1.5pt) node[right] {$C'$};
                \\fill (D') circle (1.5pt) node[left] {$D'$};
                \\fill (O) circle (1.5pt) node[below] {$O$};
                \\fill (O') circle (1.5pt) node[above] {$O'$};
            \\end{tikzpicture}
            \\end{center}''' % (edge))

            ######################################################################## Nhận biết ############################################

            # Các đáp án
            nb_da_1_d = '\\True $\\overrightarrow{AB} \\cdot \\overrightarrow{DC\'} = %s$' % edge_sq
            nb_da_1_s = '$\\overrightarrow{AB} \\cdot \\overrightarrow{DC\'} = %s$' % frac_false
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có $\\overrightarrow{AB} \\cdot \\overrightarrow{DC'} = \\overrightarrow{AB} \\cdot \\overrightarrow{AB'} = \\left| \\overrightarrow{AB} \\right| \\cdot \\left| \\overrightarrow{AB'} \\right| \\cos \\left( \\overrightarrow{AB}, \\overrightarrow{AB'} \\right) = %s \\cdot %s\\sqrt{2} \\cdot \\cos 45^\\circ = %s$.''' % (edge, edge, edge_sq))
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
            th_da_1_d = '\\True $\\overrightarrow{AB\'} \\cdot \\overrightarrow{B\'D\'} = -%s$' % edge_sq  
            th_da_1_s = '$\\overrightarrow{AB\'} \\cdot \\overrightarrow{B\'D\'} = %s$' % neg_frac_false 
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $\\left( \\overrightarrow{AB'}, \\overrightarrow{B'D'} \\right) = 180^\\circ - \\widehat{AB'D'} = 120^\\circ$, suy ra \\\\
            $\\overrightarrow{AB'} \\cdot \\overrightarrow{B'D'} = \\left| \\overrightarrow{AB'} \\right| \\cdot \\left| \\overrightarrow{B'D'} \\right| \\cos 120^\\circ = \\left( %s\\sqrt{2} \\right) \\cdot \\left( %s\\sqrt{2} \\right) \\cdot \\left( -\\frac{1}{2} \\right) = -%s$.''' % (edge, edge, edge_sq))

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
            vd_da_1_d = '\\True $\\left| \\overrightarrow{D\'A\'} + \\overrightarrow{C\'C} + \\overrightarrow{AB} \\right| = %s$' % c_true  
            vd_da_1_s = '$\\left| \\overrightarrow{D\'A\'} + \\overrightarrow{C\'C} + \\overrightarrow{AB} \\right| = %s$' % c_false  
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Ta có $\\overrightarrow{D'A'} + \\overrightarrow{C'C} + \\overrightarrow{AB} = \\overrightarrow{D'A'} + \\overrightarrow{D'D} + \\overrightarrow{D'C'} = \\overrightarrow{D'B}$. \\\\
            Suy ra $\\left| \\overrightarrow{D'A'} + \\overrightarrow{C'C} + \\overrightarrow{AB} \\right| = \\left| \\overrightarrow{D'B} \\right| = BD' = %s$.''' % c_true)

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
            vdc_da_1_d = '\\True $\\left| \\overrightarrow{OA\'} + \\overrightarrow{OB\'} + \\overrightarrow{OC\'} + \\overrightarrow{OD\'} \\right| = %s$' % d_true 
            vdc_da_1_s = '$\\left| \\overrightarrow{OA\'} + \\overrightarrow{OB\'} + \\overrightarrow{OC\'} + \\overrightarrow{OD\'} \\right| = %s$' % d_false 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có $\\overrightarrow{OA'} + \\overrightarrow{OB'} + \\overrightarrow{OC'} + \\overrightarrow{OD'} = \\left( \\overrightarrow{OA'} + \\overrightarrow{OC'} \\right) + \\left( \\overrightarrow{OB'} + \\overrightarrow{OD'} \\right) = 2\\overrightarrow{OO'} + 2\\overrightarrow{OO'} = 4\\overrightarrow{OO'}$. \\\\
            Suy ra $\\left| \\overrightarrow{OA'} + \\overrightarrow{OB'} + \\overrightarrow{OC'} + \\overrightarrow{OD'} \\right| = \\left| 4\\overrightarrow{OO'} \\right| = 4OO' = %s$.''' % d_true)

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

