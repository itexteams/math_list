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


def bt_dang2_p2_b3_c2_hh11(self):
            # Khai báo biến
            a = randint(2, 9)
            goc = 45

            # --- TÍNH TOÁN CHUẨN ---
            # I là trung điểm BC => SI vuông góc (ABC). AI = BC/2 = (a*sqrt(2))/2
            ai = a * sqrt(2) / 2
            # M là trung điểm AB => IM = AC/2 = a/2
            im = Rational(a, 2)
            # Góc giữa SI và (SAB) là góc ISH = 45 độ => SI = IM * cot(45) = IM
            si = im
            # SA = sqrt(SI^2 + AI^2) = sqrt((a/2)^2 + (a*sqrt(2)/2)^2) = a*sqrt(3)/2
            sa = sqrt(si**2 + ai**2)

            # Tính góc SAI (Góc giữa SA và mặt đáy)
            tang = si/ai
            goc1 = atan(tang)
            kq1 = goc1*180/pi
            number = Decimal(float(kq1))  # Số cần làm tròn
            kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác vuông cân tại $A$, $AB=AC=%s$, $SA=SB=SC$. Gọi $I$ là trung điểm của $BC$, $H$ là hình chiếu của $I$ lên mặt phẳng $(SAB)$.'''                 
                            %(latex(a)
                                ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $BC \\bot SA$'
            nb_da_1_s = '$BC \\bot SB$'
            nb_da_1_s1 = '$BC \\bot SC$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s,nb_da_1_s1]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''\\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                    \\clip(-1.0571466574418402,-2.7512153824748093) rectangle (5.856723559835627,4.846444196950974);
                    \\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (0.,0.)-- (5.,0.);
                    \\draw [line width=1.pt] (0.,0.)-- (3.,-2.);
                    \\draw [line width=1.pt] (3.,-2.)-- (5.,0.);
                    \\draw [line width=1.pt] (0.,0.)-- (2.,4.);
                    \\draw [line width=1.pt] (2.,4.)-- (5.,0.);
                    \\draw [line width=1.pt] (2.,4.)-- (3.,-2.);
                    \\draw [line width=1.pt] (4.,-1.)-- (2.,4.);
                    \\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (4.,-1.)-- (1.4890894879529055,-0.9927263253019368);
                    \\draw [line width=1.pt] (1.4890894879529055,-0.9927263253019368)-- (2.,4.);
                    \\draw [line width=1.pt] (3.,-2.)-- (3.499527884363254,2.000629487515662);
                    \\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (3.3116165499891106,0.7209586250272229)-- (1.4890894879529055,-0.9927263253019368);
                    \\draw (1.79197568484283,4.6) node[anchor=north west] {$S$};
                    \\draw (5,0.3) node[anchor=north west] {$A$};
                    \\draw (2.7416831322710538,-1.9154728287379732) node[anchor=north west] {$B$};
                    \\draw (-0.6,0.3) node[anchor=north west] {$C$};
                    \\draw (3.938314516030615,-0.7568297428755414) node[anchor=north west] {$M$};
                    \\draw (3.3874841965222453,2.6) node[anchor=north west] {$N$};
                    \\draw (3.3874841965222453,1.2185617477751622) node[anchor=north west] {$H$};
                    \\draw (1.146174620591638,-0.7948180407726703) node[anchor=north west] {$I$};
                \\end{tikzpicture}
            \\end{center}
            Ta có $\\heva{&SI \\bot BC \\\\& AI \\bot BC} \\Rightarrow BC \\bot (SAI) \\Rightarrow BC \\bot SA$.''')

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
            th_da_1_d = '\\True $H$ là trực tâm của tam giác $SAB$'
            th_da_1_s = '$H$ là trọng tâm của tam giác $SAB$'  
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Gọi $M$ là trung điểm của $AB$, $BN \\bot SA$ và $H=SM \\cap BN$. \\\\
                            Ta có $\\heva{&AB \\bot IM \\\\& AB \\bot SM} \\Rightarrow AB \\bot (SIM) \\Rightarrow AB \\bot IH$. \\\\
                            Ta có $\\heva{&SA \\bot BC \\\\& SA \\bot BN} \\Rightarrow SA \\bot (BCN) \\Rightarrow SA \\bot IH$.\\\\
                            Suy ra $\\heva{&IH \\bot AI \\\\& IH \\bot SA} \\Rightarrow IH \\bot (SAB)$. \\\\
                            Vậy $H$ là trực tâm của tam giác $SAB$.''')

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
            vd_da_1_d = '\\True Biết góc giữa $SI$ và $(SAB)$ bằng $%s^\\circ$. Độ dài cạnh $SA$ bằng $%s$' %(latex(goc),latex(sa))  
            vd_da_1_s = 'Biết góc giữa $SI$ và $(SAB)$ bằng $%s^\\circ$. Độ dài cạnh $SA$ bằng $%s$' %(latex(goc),latex(sa+1)) 
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải (Sửa lại logic chuẩn)
            loigiai_vd_1 = ('''Góc giữa $SI$ và $(SAB)$ bằng $%s^\\circ$. \\\\
                            Do $IH \\bot (SAB)$ nên góc giữa $\\left(SI, (SAB) \\right)=\\widehat{ISH}=%s^\\circ$.\\\\
                            Trong tam giác vuông $SIM$, ta có $SI = IM \\cdot \\cot \\widehat{ISH}$. \\\\
                            Mà $IM$ là đường trung bình của $\\triangle ABC$ suy ra $IM = \\frac{AC}{2} = %s$. \\\\
                            Suy ra $SI = %s \\cdot \\cot %s^\\circ = %s$. \\\\
                            Ta có $AI = \\frac{BC}{2} = %s$. \\\\
                            Xét tam giác $SAI$ vuông tại $I$, ta có $SA = \\sqrt{SI^2 + AI^2} = \\sqrt{(%s)^2 + (%s)^2} = %s$.'''  
                        %(latex(goc),
                        latex(goc),
                        latex(im),
                        latex(im), latex(goc), latex(si),
                        latex(ai),
                        latex(si), latex(ai), latex(sa)
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
            vdc_da_1_d = '\\True Góc giữa đường thẳng $SA$ và mặt phẳng $(ABC)$ bằng $%s^\\circ$' %(latex(kq))
            vdc_da_1_s = 'Góc giữa đường thẳng $SA$ và mặt phẳng $(ABC)$ bằng $%s^\\circ$' %(latex(kq+10))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có $\\heva{& AB \\bot IM \\\\ & AB \\bot SM} \\Rightarrow AB \\bot SI$. \\\\
                            $\\heva{& SI \\bot BC \\\\ & SI \\bot AB} \\Rightarrow SI \\bot (ABC) \\Rightarrow  \\left(SA,(ABC)\\right)=\\widehat{SAI}$. \\\\
                            Ta có $AI = %s$. \\\\
                            Xét tam giác $SAI$ có $\\tan \\widehat{SAI}=\\frac{SI}{AI}=%s \\Rightarrow \\widehat{SAI} \\approx %s^\\circ$.'''
                        %(latex(ai),
                        latex(tang),latex(kq)
                            ))

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
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
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

