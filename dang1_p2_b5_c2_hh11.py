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


def bt_dang1_p2_b5_c2_hh11(self):
            # Khai báo biến
            hinhve=('''\\begin{center} \n'''
                    '''\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                \\clip(-1.457778299136516,-0.47822429313117554) rectangle (7,5.380255055687984);
                \\draw (0.,0.)-- (4.,0.);
                \\draw [dash pattern=on 5pt off 5pt] (0.,0.)-- (2.,2.);
                \\draw [dash pattern=on 5pt off 5pt] (2.,2.)-- (6.,2.);
                \\draw (6.,2.)-- (4.,0.);
                \\draw [dash pattern=on 5pt off 5pt] (2.,5.)-- (2.,2.);
                \\draw (2.,5.)-- (4.,0.);
                \\draw (2.,5.)-- (0.,0.);
                \\draw (2.,5.)-- (6.,2.);
                \\draw [dash pattern=on 5pt off 5pt] (0.,0.)-- (6.,2.);
                \\draw [dash pattern=on 5pt off 5pt] (2.,2.)-- (4.,0.);
                \\draw [dash pattern=on 5pt off 5pt] (3.,1.)-- (3.249655172413793,1.8758620689655174);
                \\draw (1.6,5.46) node[anchor=north west] {$S$};
                \\draw (1.44,2.5) node[anchor=north west] {$A$};
                \\draw (-0.58,0.3) node[anchor=north west] {$B$};
                \\draw (6,2.5) node[anchor=north west] {$D$};
                \\draw (3.98,0.14) node[anchor=north west] {$C$};
                \\draw (2.62,0.9) node[anchor=north west] {$O$};
                \\draw (3.1,2.5) node[anchor=north west] {$H$};
            \\end{tikzpicture}'''
            '''\\end{center}\n'''
                    )
            a1=randint(4,9)
            a=2*a1
            b1=randint(4,9)
            b=2*b1
            yc=a/(sqrt(a**2+b**2))
            ycs=(a+1)/(sqrt(a**2+b**2))
            yc1=b/(sqrt(a**2+b**2))
            yc1s=(b+1)/(sqrt(a**2+b**2))
            kc=(b1*a*sqrt(2))/sqrt(a**2+2*b**2)
            kcs=(b1*sqrt(2))/sqrt(a**2+2*b**2+1)
            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$, có $SA\\bot(ABCD),SA=%s,ABCD$ là hình vuông tâm $O$ cạnh bằng $%s$.'''
                            %(latex(a),latex(b)))


            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '''\\True $SA\\bot BD$'''
            nb_da_1_s = '''$SA\\bot SB$'''
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '''\\True $SA\\bot CD$'''
            nb_da_2_s = '''$SA\\bot SC$'''
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]
            nb_da_2=random.choice(list_nb_da_2)

            nb_da_3_d = '''\\True $SA\\bot BC$'''
            nb_da_3_s = '''$SA\\bot SD$'''
            list_nb_da_3=[nb_da_3_d,nb_da_3_s]
            nb_da_3=random.choice(list_nb_da_3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2, nb_da_3]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Vì $SA\\bot(ABCD)$ mà $BD\\subset (ABCD)$ nên $SA\\bot BD$.'''
                        )
            loigiai_nb_2 = ('''Vì $SA\\bot(ABCD)$ mà $CD\\subset (ABCD)$ nên $SA\\bot CD$.'''
                        )
            loigiai_nb_3 = ('''Vì $SA\\bot(ABCD)$ mà $BC\\subset (ABCD)$ nên $SA\\bot BC$.'''
                        )
            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1, loigiai_nb_2, loigiai_nb_3]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '''\\True $AB\\bot(SAD)$'''
            th_da_1_s = '''$AB\\bot (SAC)$'''
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '''\\True $BD\\bot(SAC)$'''
            th_da_2_s = '''$BD\\bot(SAD)$'''
            list_th_da_2=[th_da_2_d,th_da_2_s]

            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $AB\\bot AD\\supset (SAD)$ (do $ABCD$ là hình vuông) $(1)$ .\\\\ \n'''
                            '''Vì $SA\\bot(ABCD)$ mà $AB\\subset (ABCD)$ nên $AB\\bot SA\\supset (SAD)$ $(2)$. \\\\ \n'''
                            '''Từ $(1),(2)$ ta có $AB\\bot(SAD)$.'''
                                        )
            loigiai_th_2 = ('''Ta có $BD\\bot AC\\supset (SAC)$ (do $ABCD$ là hình vuông) $(1)$ .\\\\ \n'''
                            '''Vì $SA\\bot(ABCD)$ mà $BD\\subset (ABCD)$ nên $BD\\bot SA\\supset (SAC)$ $(2)$. \\\\ \n'''
                            '''Từ $(1),(2)$ ta có $BD\\bot(SAC)$.'''
                                        )

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1, loigiai_th_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '''\\True côsin của góc giữa $SB$ và $(SAD)$ bằng $%s$'''%(latex(yc))
            vd_da_1_s = ''' côsin của góc giữa $SB$ và $(SAD)$ bằng $%s$'''%(latex(ycs))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '''\\True sin của góc giữa $SD$ và $(SAB)$ bằng $%s$'''%(latex(yc1))
            vd_da_2_s = ''' sin của góc giữa $SD$ và $(SAB)$ bằng $%s$'''%(latex(yc1s))
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]

            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Vì $A$ là hình chiếu vuông góc của $B$ trên mặt phẳng $SAD$ nên góc giữa $SB$ và mặt phẳng $SAD$ là $\\widehat{BSA}$. \\\\ \n'''
                            '''Xét tam giác vuông $SAB$ vuông tại $A$ ta có $SB=\\sqrt{SA^2+AB^2}=\\sqrt{%s^2+%s^2}=%s$.\\\\ \n'''
                            '''$\\cos\\widehat{BSA}=\\dfrac{SA}{SB}=\\dfrac{%s}{%s}=%s$.'''
                            %(latex(a),latex(b),latex(sqrt(a**2+b**2)),
                            latex(a),latex(sqrt(a**2+b**2)),latex(yc),)
                            )
            loigiai_vd_2 = ('''Vì $A$ là hình chiếu vuông góc của $D$ trên mặt phẳng $SAB$ nên góc giữa $SD$ và mặt phẳng $SAB$ là $\\widehat{DSA}$. \\\\ \n'''
                            '''Xét tam giác vuông $SAD$ vuông tại $A$ ta có $SD=\\sqrt{SA^2+AD^2}=\\sqrt{%s^2+%s^2}=%s$.\\\\ \n'''
                            '''$\\sin\\widehat{DSA}=\\dfrac{AD}{SD}=\\dfrac{%s}{%s}=%s$.'''
                            %(latex(a),latex(b),latex(sqrt(a**2+b**2)),
                            latex(b),latex(sqrt(a**2+b**2)),latex(yc1),)
                            )
            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1, loigiai_vd_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '''\\True Khoảng cách từ $O$ đến $SC$ bằng $%s$'''%(latex(kc))
            vdc_da_1_s = '''Khoảng cách từ $O$ đến $SC$ bằng $%s$'''%(latex(kcs))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '''\\True Khoảng cách từ $O$ đến $SC$ bằng $%s$'''%(latex(kc))
            vdc_da_2_s = '''Khoảng cách từ $O$ đến $SC$ bằng $%s$'''%(latex(kcs))
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

            vdc_da_2=random.choice(list_vdc_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1, vdc_da_2]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Kẻ $OH\\bot SC\\Rightarrow d(O,SC)=OH$.\\\\ \n'''
                            ''' $OC=\\dfrac{AC}{2}=%s\\sqrt{2};SC=\\sqrt{SA^2+AC^2}=%s$. \\\\ \n'''
                            ''' $\\Delta OHC$ đồng dạng $\\Delta SAC\\Rightarrow \\dfrac{OH}{OC}=\\dfrac{SA}{SC}\\Rightarrow OH=\\dfrac{OC\\cdot SA}{SC}=\\dfrac{%s\\sqrt{2}\\cdot %s}{%s}=%s$.'''
                            %(latex(b1),latex(sqrt(a**2+2*b**2)),
                            latex(b1),latex(a),latex(sqrt(a**2+2*b**2)),latex(kc))
                        )
            loigiai_vdc_2 = ('''Kẻ $OH\\bot SC\\Rightarrow d(O,SC)=OH$.\\\\ \n'''
                            ''' $OC=\\dfrac{AC}{2}=%s\\sqrt{2};SC=\\sqrt{SA^2+AC^2}=%s$. \\\\ \n'''
                            ''' $\\Delta OHC$ đồng dạng $\\Delta SAC\\Rightarrow \\dfrac{OH}{OC}=\\dfrac{SA}{SC}\\Rightarrow OH=\\dfrac{OC\\cdot SA}{SC}=\\dfrac{%s\\sqrt{2}\\cdot %s}{%s}=%s$.'''
                            %(latex(b1),latex(sqrt(a**2+2*b**2)),
                            latex(b1),latex(a),latex(sqrt(a**2+2*b**2)),latex(kc))
                        )
            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2]

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
                '\\loigiai{' +str(hinhve)+' \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

