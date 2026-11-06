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


def bt_dang14_p2_b2_c4_ds12(self):
            # Khai báo biến
            l1=randint(30,70)
            l2=100-l1
            t1=randint(80,95)
            h1=100-t1
            t2=randint(80,94)
            h2=100-t2
            p1=l1/100
            q1=l2/100
            p2=t1/100
            p22=h1/100
            q2=t2/100
            q22=h2/100
            pb=nsimplify(p1*p2+q1*q2)
            while l1-l2==0 or h1-h2==0:
                # Khai báo biến
                l1=randint(30,70)
                l2=100-l1
                t1=randint(80,95)
                h1=100-t1
                t2=randint(80,94)
                h2=100-t2
                p1=l1/100
                q1=l2/100
                p2=t1/100
                p22=h1/100
                q2=t2/100
                q22=h2/100
                pb=nsimplify(p1*p2+q1*q2)

            # Nội dung câu hỏi
            noidungcauhoi = ('Một xưởng máy sử dụng một loại linh kiện được sản xuất từ hai cơ sở I và II$zz$ Số linh kiện do cơ sở I sản xuất chiếm $%spht$, số linh kiện do cơ sở II sản xuất chiếm $%spht$$zz$ '
                            'Tỉ lệ linh kiện đạt tiêu chuẩn của cơ sở I, cơ sở II lần lượt là $%spht$, $%spht$$zz$ '
                            'Kiểm tra ngẫu nhiên $1$ linh kiện ở xưởng máy$zz$ Xét các biến cố:\\\\ \n'
                            '\\hspace*{1cm} $A_{1}$: "Linh kiện được kiểm tra do cơ sở I sản xuất";\\\\ \n'
                            '\\hspace*{1cm} $A_{2}$: "Linh kiện được kiểm tra do cơ sở II sản xuất";\\\\ \n'
                            '\\hspace*{1cm} $B$: "Linh kiện được kiểm tra đạt tiêu chuẩn"$zz$'
                            %(latex(l1),latex(l2),latex(t1),latex(t2))
                            )
            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d =  '\\True $\\mathrm{P}(A_{1})=%s$'%(latex(p1))
            nb_da_1_s = '$\\mathrm{P}(A_{1})=%s$'%(latex(q1))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d =  '\\True $\\mathrm{P}(A_{2})=%s$'%(latex(q1))
            nb_da_2_s = '$\\mathrm{P}(A_{2})=%s$'%(latex(p1))
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]
            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1,nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('Theo bài ta có sơ đồ hình cây\\\\ \n'
                            '\\begin{center}'
                            '\\begin{tikzpicture}[line join = round, line cap = round, >=stealth, font=\\footnotesize, scale=1]\n'
                '\\begin{scope}[every node/$zz$style={draw, rounded corners=5pt}]\n'
                    '\\node (A) at (0,0){Kiểm tra 1 linh kiện};\n'
                    '\\def \\gocA{30}\n'
                    '\\def \\kcA{4}\n'
                    '\\node (B1) at ($(A)+(\\gocA:\\kcA)$){$A_{1}$};\n'
                    '\\node (B2) at ($(A)+(-\\gocA:\\kcA)$){$A_{2}$};\n'
                    '\\def \\gocB{15}\n'
                    '\\def \\kcB{4}\n'
                    '\\node (B11) at ($(B1)+(\\gocB:\\kcB)$){$B$};\n'
                    '\\node (B12) at ($(B1)+(-\\gocB:\\kcB)$){$\\overline{B}$};\n'
                    '\\node (B21) at ($(B2)+(\\gocB:\\kcB)$){$B$};\n'
                    '\\node (B22) at ($(B2)+(-\\gocB:\\kcB)$){$\\overline{B}$};\n'
                '\\end{scope}\n'
                '\\begin{scope}[every node/$zz$style={midway,sloped},every path/$zz$style={->}]\n'
                    '\\draw (A)--(B1) node[above]{$\\mathrm{P}(A_{1})=$\\fbox{$%s$}};\n'
                    '\\draw (A)--(B2) node[below]{$\\mathrm{P}(A_{2})=$\\fbox{$%s$}};\n'
                    '\\draw (B1)--(B11) node[above]{$\\mathrm{P}(B|A_{1})=$\\fbox{$%s$}};\n'
                    '\\draw (B1)--(B12) node[below]{$\\mathrm{P}(\\overline{B}|A_{1})=$\\fbox{$%s$}};\n'
                    '\\draw (B2)--(B21) node[above]{$\\mathrm{P}(B|A_{2})=$\\fbox{$%s$}};\n'
                    '\\draw (B2)--(B22) node[below]{$\\mathrm{P}(\\overline{B}|A_{2})=$\\fbox{$%s$}};\n'
                '\\end{scope}\n'
                '\\end{tikzpicture}\n'
                '\\end{center}\n'
                'Ta có $\\mathrm{P}(A_{1})=%s$$zz$'
                %(latex(p1),latex(q1),latex(p2),latex(p22),latex(q2),latex(q22),latex(p1))
                        )
            loigiai_nb_2 =  ('Theo bài ta có sơ đồ hình cây\\\\ \n'
                            '\\begin{center}'
                            '\\begin{tikzpicture}[line join = round, line cap = round, >=stealth, font=\\footnotesize, scale=1]\n'
                '\\begin{scope}[every node/$zz$style={draw, rounded corners=5pt}]\n'
                    '\\node (A) at (0,0){Kiểm tra 1 linh kiện};\n'
                    '\\def \\gocA{30}\n'
                    '\\def \\kcA{4}\n'
                    '\\node (B1) at ($(A)+(\\gocA:\\kcA)$){$A_{1}$};\n'
                    '\\node (B2) at ($(A)+(-\\gocA:\\kcA)$){$A_{2}$};\n'
                    '\\def \\gocB{15}\n'
                    '\\def \\kcB{4}\n'
                    '\\node (B11) at ($(B1)+(\\gocB:\\kcB)$){$B$};\n'
                    '\\node (B12) at ($(B1)+(-\\gocB:\\kcB)$){$\\overline{B}$};\n'
                    '\\node (B21) at ($(B2)+(\\gocB:\\kcB)$){$B$};\n'
                    '\\node (B22) at ($(B2)+(-\\gocB:\\kcB)$){$\\overline{B}$};\n'
                '\\end{scope}\n'
                '\\begin{scope}[every node/$zz$style={midway,sloped},every path/$zz$style={->}]\n'
                    '\\draw (A)--(B1) node[above]{$\\mathrm{P}(A_{1})=$\\fbox{$%s$}};\n'
                    '\\draw (A)--(B2) node[below]{$\\mathrm{P}(A_{2})=$\\fbox{$%s$}};\n'
                    '\\draw (B1)--(B11) node[above]{$\\mathrm{P}(B|A_{1})=$\\fbox{$%s$}};\n'
                    '\\draw (B1)--(B12) node[below]{$\\mathrm{P}(\\overline{B}|A_{1})=$\\fbox{$%s$}};\n'
                    '\\draw (B2)--(B21) node[above]{$\\mathrm{P}(B|A_{2})=$\\fbox{$%s$}};\n'
                    '\\draw (B2)--(B22) node[below]{$\\mathrm{P}(\\overline{B}|A_{2})=$\\fbox{$%s$}};\n'
                '\\end{scope}\n'
                '\\end{tikzpicture}\n'
                '\\end{center}\n'
                'Ta có $\\mathrm{P}(A_{2})=%s$$zz$'
                %(latex(p1),latex(q1),latex(p2),latex(p22),latex(q2),latex(q22),latex(q1))
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
            th_da_1_d = '\\True $\\mathrm{P}(B|A_{1})=%s$'%(latex(p2))
            th_da_1_s ='$\\mathrm{P}(B|A_{1})=%s$'%(latex(p22))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True $\\mathrm{P}(B|A_{2})=%s$'%(latex(q2))
            th_da_2_s ='$\\mathrm{P}(B|A_{2})=%s$'%(latex(q22))
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1,th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('$\\mathrm{P}(B|A_{1})=%s$'%(latex(p2))
                        )
            loigiai_th_2 = ('$\\mathrm{P}(B|A_{2})=%s$'%(latex(q2))
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
            vd_da_1_d = '\\True $\\mathrm{P}(\\overline{B}|A_{1})=%s$'%(latex(p22))
            vd_da_1_s = '$\\mathrm{P}(\\overline{B}|A_{1})=%s$'%(latex(p2))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True $\\mathrm{P}(\\overline{B}|A_{2})=%s$'%(latex(q22))
            vd_da_2_s = '$\\mathrm{P}(\\overline{B}|A_{2})=%s$'%(latex(q2))
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]
            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1,vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 = ('$\\mathrm{P}(\\overline{B}|A_{1})=%s$'%(latex(p22)))
            loigiai_vd_2 = ('$\\mathrm{P}(\\overline{B}|A_{2})=%s$'%(latex(q22)))

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
                            '\\hspace*{1cm}$\\mathrm{P}(B)=\\mathrm{P}(A_{1})\\cdot\\mathrm{P}(B|A_{1})+\\mathrm{P}(A_{2})\\cdot\\mathrm{P}(B|A_{2})=%s\\cdot %s+%s\\cdot %s=%s$$zz$'
                            %(latex(p1),latex(p2),latex(q1),latex(q2),latex(pb))
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

