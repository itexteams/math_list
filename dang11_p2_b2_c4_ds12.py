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


def bt_dang11_p2_b2_c4_ds12(self):
            # Khai báo biến
            lt=randint(30,70)
            lx=100-lt
            ht=randint(1,5)
            kt=100-ht
            hx=randint(1,5)
            kx=100-hx
            pt=lt/100
            px=lx/100
            pba=kt/100
            pb_a=ht/100
            p_ba=kx/100
            p_b_a=hx/100
            pb=nsimplify(pt*pba+px*p_ba)
            while lt-lx==0 or ht-hx==0:
                lt=randint(30,70)
                lx=100-lt
                ht=randint(1,5)
                kt=100-ht
                hx=randint(1,5)
                kx=100-hx
                pt=lt/100
                px=lx/100
                pba=kt/100
                pb_a=ht/100
                p_ba=kx/100
                p_b_a=hx/100
                pb=nsimplify(pt*pba+px*p_ba)

            # Nội dung câu hỏi
            noidungcauhoi = ('Một cửa hàng có hai loại bóng đèn Led, trong đó $%spht$ bóng đèn Led màu trắng và $%spht$ bóng đèn Led màu xanh, các bóng đèn có cùng kích thước như nhau$zz$ '
                            'Các bóng đèn Led màu trắng có tỉ lệ hỏng là $%spht$ và các bóng đèn Led màu xanh có tỉ lệ hỏng là $%spht$$zz$ '
                            'Một khách hàng chọn mua ngẫu nhiên $1$ bóng đèn Led từ cửa hàng$zz$ Xét các biến cố:\\\\ \n'
                            '\\hspace*{1cm} $A$: "Khách hàng chọn được bóng đèn Led màu trắng"\\\\ \n'
                            '\\hspace*{1cm} $B$: "Khách hàng chọn được bóng đèn Led không hỏng"$zz$'
                            %(latex(lt),latex(lx),latex(ht),latex(hx))
                            )
            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d =  '\\True $\\mathrm{P}(A)=%s$'%(latex(pt))
            nb_da_1_s = '$\\mathrm{P}(A)=%s$'%(latex(1-pt))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d =  '\\True $\\mathrm{P}(\\overline{A})=%s$'%(latex(px))
            nb_da_2_s = '$\\mathrm{P}(\\overline{A})=%s$'%(latex(1-px))
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]
            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1,nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('Theo bài ta có sơ đồ hình cây\\\\ \n'
                            '\\begin{center}'
                            '\\begin{tikzpicture}[line join = round, line cap = round, >=stealth, font=\\footnotesize, scale=1]\n'
                '\\begin{scope}[every node/$zz$style={draw, rounded corners=5pt}]\n'
                    '\\node (A) at (0,0){Chọn mua 1 bóng};\n'
                    '\\def \\gocA{30}\n'
                    '\\def \\kcA{4}\n'
                    '\\node (B1) at ($(A)+(\\gocA:\\kcA)$){$A$};\n'
                    '\\node (B2) at ($(A)+(-\\gocA:\\kcA)$){$\\overline{A}$};\n'
                    '\\def \\gocB{15}\n'
                    '\\def \\kcB{4}\n'
                    '\\node (B11) at ($(B1)+(\\gocB:\\kcB)$){$B$};\n'
                    '\\node (B12) at ($(B1)+(-\\gocB:\\kcB)$){$\\overline{B}$};\n'
                    '\\node (B21) at ($(B2)+(\\gocB:\\kcB)$){$B$};\n'
                    '\\node (B22) at ($(B2)+(-\\gocB:\\kcB)$){$\\overline{B}$};\n'
                '\\end{scope}\n'
                '\\begin{scope}[every node/$zz$style={midway,sloped},every path/$zz$style={->}]\n'
                    '\\draw (A)--(B1) node[above]{$\\mathrm{P}(A)=$\\fbox{$%s$}};\n'
                    '\\draw (A)--(B2) node[below]{$\\mathrm{P}(\\overline{A})=$\\fbox{$%s$}};\n'
                    '\\draw (B1)--(B11) node[above]{$\\mathrm{P}(B|A)=$\\fbox{$%s$}};\n'
                    '\\draw (B1)--(B12) node[below]{$\\mathrm{P}(\\overline{B}|A)=$\\fbox{$%s$}};\n'
                    '\\draw (B2)--(B21) node[above]{$\\mathrm{P}(B|\\overline{A})=$\\fbox{$%s$}};\n'
                    '\\draw (B2)--(B22) node[below]{$\\mathrm{P}(\\overline{B}|\\overline{A})=$\\fbox{$%s$}};\n'
                '\\end{scope}\n'
                '\\end{tikzpicture}\n'
                '\\end{center}\n'
                'Ta có $\\mathrm{P}(A)=%s$$zz$'
                %(latex(pt),latex(px),latex(pba),latex(pb_a),latex(p_ba),latex(p_b_a),latex(pt))
                        )
            loigiai_nb_2 =  ('Theo bài ta có sơ đồ hình cây\\\\ \n'
                            '\\begin{center}\n'
                            '\\begin{tikzpicture}[line join = round, line cap = round, >=stealth, font=\\footnotesize, scale=1]\n'
                '\\begin{scope}[every node/$zz$style={draw, rounded corners=5pt}]\n'
                    '\\node (A) at (0,0){Chọn mua 1 bóng};\n'
                    '\\def \\gocA{30}\n'
                    '\\def \\kcA{4}\n'
                    '\\node (B1) at ($(A)+(\\gocA:\\kcA)$){$A$};\n'
                    '\\node (B2) at ($(A)+(-\\gocA:\\kcA)$){$\\overline{A}$};\n'
                    '\\def \\gocB{15}\n'
                    '\\def \\kcB{4}\n'
                    '\\node (B11) at ($(B1)+(\\gocB:\\kcB)$){$B$};\n'
                    '\\node (B12) at ($(B1)+(-\\gocB:\\kcB)$){$\\overline{B}$};\n'
                    '\\node (B21) at ($(B2)+(\\gocB:\\kcB)$){$B$};\n'
                    '\\node (B22) at ($(B2)+(-\\gocB:\\kcB)$){$\\overline{B}$};\n'
                '\\end{scope}\n'
                '\\begin{scope}[every node/$zz$style={midway,sloped},every path/$zz$style={->}]\n'
                    '\\draw (A)--(B1) node[above]{$\\mathrm{P}(A)=$\\fbox{$%s$}};\n'
                    '\\draw (A)--(B2) node[below]{$\\mathrm{P}(\\overline{A})=$\\fbox{$%s$}};\n'
                    '\\draw (B1)--(B11) node[above]{$\\mathrm{P}(B|A)=$\\fbox{$%s$}};\n'
                    '\\draw (B1)--(B12) node[below]{$\\mathrm{P}(\\overline{B}|A)=$\\fbox{$%s$}};\n'
                    '\\draw (B2)--(B21) node[above]{$\\mathrm{P}(B|\\overline{A})=$\\fbox{$%s$}};\n'
                    '\\draw (B2)--(B22) node[below]{$\\mathrm{P}(\\overline{B}|\\overline{A})=$\\fbox{$%s$}};\n'
                '\\end{scope}\n'
                '\\end{tikzpicture}\n'
                '\\end{center}\n'
                'Ta có  $\\mathrm{P}(\\overline{A})=%s$$zz$'
                %(latex(pt),latex(px),latex(pba),latex(pb_a),latex(p_ba),latex(p_b_a),latex(px))
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1,loigiai_nb_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $\\mathrm{P}(B|A)=%s$'%(latex(pba))
            th_da_1_s ='$\\mathrm{P}(B|A)=%s$'%(latex(1-pba))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True $\\mathrm{P}(B|\\overline{A})=%s$'%(latex(p_ba))
            th_da_2_s ='$\\mathrm{P}(B|\\overline{A})=%s$'%(latex(1-p_ba))
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1,th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('$\\mathrm{P}(B|A)=%s$$zz$'%(latex(pba))
                        )
            loigiai_th_2 = ('$\\mathrm{P}(B|\\overline{A})=%s$$zz$'%(latex(p_ba))
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1,loigiai_th_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $\\mathrm{P}(\\overline{B}|A)=%s$'%(latex(pb_a))
            vd_da_1_s = '$\\mathrm{P}(\\overline{B}|A)=%s$'%(latex(1-pb_a))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True $\\mathrm{P}(\\overline{B}|\\overline{A})=%s$'%(latex(p_b_a))
            vd_da_2_s = '$\\mathrm{P}(\\overline{B}|\\overline{A})=%s$'%(latex(1-p_b_a))
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]
            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1,vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 = ('$\\mathrm{P}(\\overline{B}|A)=%s$$zz$'%(latex(pb_a)))
            loigiai_vd_2 = ('$\\mathrm{P}(\\overline{B}|\\overline{A})=%s$$zz$'%(latex(p_b_a)))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1,loigiai_vd_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d ='\\True $\\mathrm{P}(B)=%s$'%(latex(pb))
            vdc_da_1_s = ' $\\mathrm{P}(B)=%s$'%(latex(1-pb))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Áp dụng công thức xác suất toàn phần ta có\\\\ \n'
                            '\\hspace*{1cm}$\\mathrm{P}(B)=\\mathrm{P}(A)\\cdot\\mathrm{P}(B|A)+\\mathrm{P}(\\overline{A})\\cdot\\mathrm{P}(B|\\overline{A})=%s\\cdot %s+%s\\cdot %s=%s$$zz$'
                            %(latex(pt),latex(pba),latex(px),latex(p_ba),latex(pb))
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('.',',').replace('$zz$','.').replace('pht','\\%')
            return content

