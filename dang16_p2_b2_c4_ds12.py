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


def bt_dang16_p2_b2_c4_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a=randint(10,40)
                p1=a/100
                p11=1-p1
                b=randint(10,30)
                p21=b/100
                p12=1-p21
                q21=p21
                q22=p12
                pb=p1*p12+p11*q21
                p_b=1-pb
                pp1=(p11*q22)/p_b
                pl=round(pp1-0.06,2)



                # Nội dung câu hỏi
                noidungcauhoi = ('Một phần mềm nhận diện tin nhắn quảng cáo trên điện thoại bằng cách dựa theo từ khoá để đánh dấu một số tin nhắn được gửi đến$zz$ '
                                'Qua một thời gian sử dụng, người ta thấy rằng trong số tất cả các tin nhắn được gửi đến, có $%spht$ số tin nhắn bị đánh dấu$zz$ Trong số các tin nhắn bị đánh dấu, '
                                'có $%spht$ số tin nhắn không phải là quảng cáo$zz$ Trong số các tin nhắn không bị đánh dấu, có $%spht$ số tin nhắn là quảng cáo$zz$\\\\ \n'
                                'Chọn ngẫu nhiên một tin nhắn được gửi đến điện thoại$zz$'
                                %(latex(a),latex(b),latex(b)
                                )
                                )
                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d =  '\\True Xác suất để tin nhắn đó không bị đánh dấu bằng $%s$'%(latex(p11))
                nb_da_1_s = ' Xác suất để tin nhắn đó không bị đánh dấu bằng $%s$'%(latex(p1))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Xét các biến cố\\\\ \n'
                        '\\hspace*{1cm} $A$: "Chọn được tin nhắn bị đánh dấu";\\\\ \n'
                        '\\hspace*{1cm} $B$: "Chọn được tin quảng cáo"$zz$\\\\ \n'

                    'Theo bài ta có sơ đồ hình cây\\\\ \n'
                                '\\begin{center}'
                                '\\begin{tikzpicture}[line join = round, line cap = round, >=stealth, font=\\footnotesize, scale=1]\n'
                    '\\begin{scope}[every node/$zz$style={draw, rounded corners=5pt}]\n'
                        '\\node (A) at (0,0){Chọn $1$ tin nhắn};\n'
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
                    'Ta có $\\mathrm{P}(\\overline{A})=%s$$zz$'
                    %(latex(p1),latex(p11),latex(p12),latex(p21),latex(q21),latex(q22),latex(p11))
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
                th_da_1_d = '\\True Xác suất để tin nhắn đó không phải là quảng cáo, biết rằng nó không bị đánh dấu, bằng $%s$'%(latex(q22))
                th_da_1_s ='Xác suất để tin nhắn đó không phải là quảng cáo, biết rằng nó không bị đánh dấu, bằng $%s$'%(latex(q21))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('$\\mathrm{P}(\\overline{B}|\\overline{A})=%s$$zz$'%(latex(q22))
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
                vd_da_1_d = '\\True Xác suất để tin nhắn đó không phải là quảng cáo bằng $%s$'%(latex(p_b))
                vd_da_1_s =  'Xác suất để tin nhắn đó không phải là quảng cáo bằng $%s$'%(latex(pb))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                vd_da_2_d = '\\True Xác suất để tin nhắn đó không phải là quảng cáo bằng $%s$'%(latex(p_b))
                vd_da_2_s = 'Xác suất để tin nhắn đó không phải là quảng cáo bằng $%s$'%(latex(pb))
                list_vd_da_2=[vd_da_2_d,vd_da_2_s]
                vd_da_2=random.choice(list_vd_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 =  ('Áp dụng công thức xác suất toàn phần ta có\\\\ \n'
                                '\\hspace*{1cm}$\\mathrm{P}(\\overline{B})=\\mathrm{P}(A)\\cdot\\mathrm{P}(\\overline{B}|A)+\\mathrm{P}(\\overline{A})\\cdot\\mathrm{P}(\\overline{B}|\\overline{A})=%s\\cdot %s+%s\\cdot %s=%s$$zz$'
                                %(latex(p1),latex(p21),latex(p11),latex(q22),latex(p_b))
                            )

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
                vdc_da_1_d ='\\True Xác suất để tin nhắn đó không bị đánh dấu, biết rằng nó không phải là quảng cáo, lớn hơn $%s$'%(latex(pl))
                vdc_da_1_s = 'Xác suất để tin nhắn đó không bị đánh dấu, biết rằng nó không phải là quảng cáo, nhỏ hơn $%s$'%(latex(pl))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ( 'Áp dụng công thức Bayes ta được\\\\ \n'
                                '\\hspace*{1cm}$\\mathrm{P}(\\overline{A}|\\overline{B})=\\dfrac{\\mathrm{P}(\\overline{A})}{\\mathrm{P}(\\overline{B})}\\cdot\\mathrm{P}(\\overline{B}|\\overline{A})=\\dfrac{%s}{%s}\\cdot %s=%s>%s$$zz$'
                                %(latex(p11),latex(p_b),latex(q22),latex(pp1),latex(pl))
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

